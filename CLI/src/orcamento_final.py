from pathlib import Path
import os
import json


def create_file_bd(file_name: str) -> None | str:
    """
    Verifica se o arquivo de configuração existe, caso nao exista
    gera o arquivo com uma lista vazia "[]"

    @param file_name: str -> Caminho completo do arquivo onde deve ser criado.
    @return str -> Se o arquivo não existe e é criado, retorna uma msg de sucesso.
    @return None -> Se o arquivo existir, não retorna nada, apenas se existir algum erro.
    """
    FILE_JSON_NAME = os.path.basename(file_name)
    data = []
    if not os.path.exists(file_name):
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
                return f"Arquivo {FILE_JSON_NAME} criado com sucesso!"
        except Exception as e:
            return f"Não foi possivel gerar o Arquivo {FILE_JSON_NAME}: {e}"


def load_data(file_name: str) -> list:
    FILE_JSON_NAME = os.path.basename(file_name)
    """
    Carrega os dados do arquivo json.
    @param file_materiais str -> Caminho completo do arquivo json.
    @return list -> Retorna uma lista de dicionarios
    """
    lista_items = []
    if os.path.exists(file_name):
        try:
            # Carrega os dados do arquivo json de materiais e adiciona em uma variavel
            with open(file_name, "r", encoding="utf-8") as file:
                read_file = file.read()
                data = json.loads(read_file)
                for items in data:
                    lista_items.append(items)
        except Exception as e:
            print(f"Erro ao ler os dados do arquivo{FILE_JSON_NAME}: {e}")
    else:
        # Cria o arquivo vazio caso ele não exista.
        create_file_bd(file_name)

    return lista_items


def update_file_bd(file_name: str, data: list) -> str:
    """
    Faz a atualização do arquivo de configuração, com as novas mudanças.

    @param file_name: str -> Caminho completo do arquivo para realizar as mudanças.
    @param data: list -> A lista com as informações para salvar no arquivo json com as mudanças.
    @return str -> Retorna uma msg de sucesso.

    """
    FILE_JSON_NAME = os.path.basename(file_name)
    lista = load_data(file_name)

    if len(lista) > 0:
        lista.extend(data)
    else:
        lista = data
        print(f"Nenhum dado no arquivo {FILE_JSON_NAME}")

    if os.path.exists(file_name):
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(lista, file, indent=2)
                return f"Arquivo {FILE_JSON_NAME} atualizado com sucesso!"
        except Exception as e:
            return f"Não foi possivel atualizar o Arquivo {FILE_JSON_NAME}: {e}"


# Construindo o json com  as informações completas para usar nos calculos do orçamento final
def add_orcamento(
        orcamento_id: int, nome: str,
        mao_de_obra_info: float,
        total_custo_fixo: float,
        valor_total_horas_min_base: list,
        lista_materiais: list,

        lista_custo_fixo: list,
        lista_mao_de_obra: list,

) -> list:

    lista_materiais_selecionado = []

    for materiais in lista_materiais:
        for key, value in materiais.items():
            if (key == "material_status" and value):
                lista_materiais_selecionado.append(materiais)

    lista_orcamento = [
        {
            "orcamento_id": orcamento_id,
            "orcamento_nome": nome,
            "orcamento_valor_mao_de_obra": mao_de_obra_info,
            "orcamento_valor_custo_fixo": total_custo_fixo,
            "orcamento_valor_hora_base": valor_total_horas_min_base,

            "orcamento_materiais": lista_materiais_selecionado,
            "orcamento_custo_fixo": lista_custo_fixo,
            "orcamento_mao_de_obra": lista_mao_de_obra,
            "orcamento_final": (mao_de_obra_info + total_custo_fixo)
        }
    ]

    return lista_orcamento


# Valor total produtos
def valor_total_materiais(lista_materiais: list) -> float:
    lista = []
    valor_total = 0

    for materiais in lista_materiais:
        for key, value in materiais.items():
            if (key == "material_status" and value):
                lista.append(materiais)

    for total in lista:
        for key, value in total.items():
            if key == "material_qntd_usado_preco":
                valor_total += value

    return valor_total


# Valor total horas trabalhados
def valor_horas_trabalhados(lista_renda_mensal: list) -> list:
    valor_hora = 0
    valor_minuto = 0

    for renda_mensal in lista_renda_mensal:
        for key, value in renda_mensal.items():
            if key == "renda_mensal_valor_total_hora":
                valor_hora += value
            if key == "renda_mensal_valor_total_minuto":
                valor_minuto += value

    return [{
        "renda_mensal_valor_total_hora": valor_hora,
        "renda_mensal_valor_total_minuto": valor_minuto,
    }]


# Valor mao de obra
def valor_mao_de_obra_horas_trabalhados(lista_mao_de_obra: list, valor_hora_minuto: list):
    porcentagem = None
    horas = None
    minutos = None
    taxa_de_urgencia = None
    valor_hora = 0
    valor_minuto = 0

    lista = []

    for mao_de_obra in lista_mao_de_obra:
        for key, value in mao_de_obra.items():
            if (key == "mao_de_obra_status"):
                lista.append(mao_de_obra)

    for item in lista:
        for key, value in item.items():
            if key == "mao_de_obra_porcentagem":
                porcentagem = value
            elif key == "mao_de_obra_horas_trabalhadaos":
                horas = value
            elif key == "mao_de_obra_minutos_trabalhados":
                minutos = value
            elif key == "mao_de_obra_taxa_de_urgencia":
                taxa_de_urgencia = value

    for valor_tempo in valor_hora_minuto:
        for key, value in valor_tempo.items():
            if key == "renda_mensal_valor_total_hora":
                valor_hora = value
            elif key == "renda_mensal_valor_total_minuto":
                valor_minuto = value

    # Calcula o valor de trabalho tanto das horas, minutos e são somados no final
    valor_total_tempo = ((horas * valor_hora) + (minutos * valor_minuto))

    # Calcula o valor da taxa de urgencia e soma com o valor do tempo de trabalho
    valor_tempo_urgencia = (
        valor_total_tempo + taxa_de_urgencia)

    # Adiciona a porcentagem  no valor do tempo de trabalhos somado a taxa de urgencia.
    valor_porcentagem_tempo_urgencia = (
        valor_tempo_urgencia * porcentagem) / 100 + valor_tempo_urgencia
    return valor_porcentagem_tempo_urgencia

# Total custo fixo (materiais + despesas fixas)


def valor_custo_fixo(lista_custo_fixo: list, valor_total_materiais: float, total_projetos_mes: int):
    valor_por_projeto = 0

    for custo in lista_custo_fixo:
        for key, value in custo.items():
            if key == "custo_fixo_valor_por_projeto":
                valor_por_projeto += value
    return (valor_total_materiais + valor_por_projeto)

# Valor final orçamento


def orcamento_projeto(lista_orcamento: list, orcamento_id: int):
    valor_total_orcamento = 0
    orcamento_selecionado = []

    # Seleciona o orcamento correto para calcular o valor final do projeto.
    for lista in lista_orcamento:
        for key, value in lista.items():
            if key == "orcamento_id" and value == orcamento_id:
                orcamento_selecionado.append(lista)

    # Faz os calculos usando o orcamento selecionado
    for oc in orcamento_selecionado:
        for key, value in oc.items():
            if key == "orcamento_final":
                valor_total_orcamento = value

    return valor_total_orcamento


# taxa de urgencia
if __name__ == "__main__":
    cwd = Path.cwd()
    bd_folder = Path(cwd, "bd")

    # File json materiais
    file_materiais = f"{bd_folder}/lista_materiais.json"
    # Dados do arquivo convertido em lista com dicionarios para usar no sistema
    lista_materiais = load_data(file_materiais)

    file_custo_fixo = f"{bd_folder}/teste_custo_fixo.json"
    lista_custo_fixo = load_data(file_custo_fixo)

    file_mao_de_obra = f"{bd_folder}/mao_de_obra.json"
    lista_mao_de_obra = load_data(file_mao_de_obra)

    file_renda_mensal = f"{bd_folder}/renda_mensal_base.json"
    lista_renda_mensal = load_data(file_renda_mensal)

    file_orcamento = f"{bd_folder}/orcamento.json"
    lista_orcamento = load_data(file_orcamento)

    # Calcula o valor total utilizado em materiais
    valor_total_materiais = valor_total_materiais(lista_materiais)
    # Retorna o valor gasto em materiais
    print("Valor Materiais: ", valor_total_materiais)

    # Calcula o valor total de horas no projeto.
    # Valor da hora e minuto trabalhados
    valor_total_horas_min = valor_horas_trabalhados(lista_renda_mensal)
    for renda in valor_total_horas_min:
        print("Valor Hora: ", renda['renda_mensal_valor_total_hora'])
        print("Valor Minuto: ", renda['renda_mensal_valor_total_minuto'])

    # Calcular o valor da mão de obra
    mao_de_obra_info = valor_mao_de_obra_horas_trabalhados(
        lista_mao_de_obra, valor_total_horas_min)
    print("Mão de Obra: ", mao_de_obra_info)  # Valor da mão de obra

    # Valor do custo fixo (materiais usados + despesas)
    total_projetos_mes = 20

    total_custo_fixo = valor_custo_fixo(
        lista_custo_fixo, valor_total_materiais, total_projetos_mes)
    # Retorna o valor de custo fixo (materiais + despesas)
    print("Custo Fixo: ", total_custo_fixo)

    # Orçamento final do projeto (Valor final)
    orcamento1 = orcamento_projeto(lista_orcamento, 5)
    print("Orçamento Final: ", orcamento1)  # Valor do orçamento final

    #  Cadastro dos dados do orçamento
    orcamento1 = add_orcamento(
        orcamento_id=5,
        nome="Orcamento5",
        mao_de_obra_info=mao_de_obra_info,
        total_custo_fixo=total_custo_fixo,
        valor_total_horas_min_base=valor_total_horas_min,
        lista_materiais=lista_materiais,
        lista_custo_fixo=lista_custo_fixo,
        lista_mao_de_obra=lista_mao_de_obra
    )

    # Atualizar o arquivo com as novas informações
    # update = update_file_bd(file_orcamento, orcamento1)
    # update = update_file_bd(file_orcamento, orcamento2)
    # print(update)
    # print(lista_orcamento)

    print()
