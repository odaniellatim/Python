import re
import os


def corrigir_e_sobrescrever_srt(caminho_arquivo):
    """Lê um arquivo srt, corrige as sobreposições e sobrescreve o original."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex para encontrar os tempos
        pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")
        matches = list(pattern.finditer(content))

        if not matches:
            return  # Pula se não encontrar timestamps no padrão srt

        new_content = list(content)

        # Percorre os blocos comparando o fim do atual com o início do próximo
        for i in range(len(matches) - 1):
            end_current = matches[i].group(2)
            start_next = matches[i + 1].group(1)

            if end_current > start_next:
                # Onde o tempo de fim atual começa e termina na string original
                start_pos = matches[i].start(2)
                end_pos = matches[i].end(2)
                # Substitui pelo tempo de início da próxima legenda
                new_content[start_pos:end_pos] = list(start_next)

        # Salva as alterações no próprio arquivo original
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("".join(new_content))

        print(f"✓ Corrigido: {os.path.basename(caminho_arquivo)}")

    except Exception as e:
        print(f"x Erro ao processar {caminho_arquivo}: {e}")


def processar_pasta(caminho_da_pasta):
    # Verifica se a pasta existe
    if not os.path.exists(caminho_da_pasta):
        print(f"Erro: A pasta '{caminho_da_pasta}' não foi encontrada.")
        return

    # Lista todos os arquivos da pasta
    arquivos = os.listdir(caminho_da_pasta)

    # Filtra apenas os arquivos com extensão .srt
    legendas = [f for f in arquivos if f.lower().endswith(".srt")]

    if not legendas:
        print("Nenhum arquivo .srt encontrado na pasta.")
        return

    print(f"Iniciando correção de {len(legendas)} arquivos...\n")

    for nome_arquivo in legendas:
        caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo)
        corrigir_e_sobrescrever_srt(caminho_completo)

    print("\nProcesso finalizado.")


# --- CONFIGURAÇÃO ---
diretorio_alvo = "/home/odaniellatim/Documentos/GitHub/Python/legenda/"
processar_pasta(diretorio_alvo)
