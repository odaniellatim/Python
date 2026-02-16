Vou te ensinar uma técnica prática para identificar conexões entre classes. Não vou te dar o diagrama pronto — vou te mostrar **como pensar** para chegar nele.

---

## 🎯 A Técnica: "Pergunte ao Objeto"

Em vez de pensar "como conecto tudo?", faça cada classe **responder perguntas** sobre si mesma.

---

## Passo 1: Isole cada classe e faça-a falar

### **Menu Front**

> "Eu sou a **interface**. Eu mostro telas e capturo cliques. Eu não calculo nada, só **pergunto** para outras classes e **mostro** o resultado."

**Pergunta que ele faz:** "Ei, Sistema, qual a média de vendas deste mês?"

---

### **Usuário**

> "Eu sou o **dono da conta**. Eu tenho senha, nome, email. Mas o mais importante: eu **possuo** coisas."

**Perguntas que ele responde:**

- "Quais produtos eu vendo?" → Olho meu catálogo
- "Quanto paguei de contas?" → Olho minhas despesas
- "Quanto vendi em janeiro?" → Olho meu histórico

**Conexão identificada:** Usuário **tem** catálogo, despesas e histórico.

---

### **Catálogo de Produtos**

> "Eu sou uma **lista de produtos disponíveis**. Cada produto sabe: nome, custo pra fazer, preço de venda."

**Pergunta que responde:** "Quanto lucro dá vender uma caneca?" → Preço menos custo.

**Conexão identificada:** Catálogo **pertence a** um usuário. Sem usuário, não existe catálogo pessoal.

---

### **Contas a Pagar (Despesas)**

> "Eu sou uma **lista de contas do mês**. Cada conta tem: nome, valor, vencimento, pago/não pago."

**Pergunta que responde:** "Quanto preciso arrecadar este mês?" → Soma dos valores não pagos.

**Conexão identificada:** Despesa **pertence a** um usuário. É a conta **dele**, não de outro.

---

### **Histórico de Vendas**

> "Eu sou um **registro do que já aconteceu**. Cada entrada diz: em qual mês, qual produto, quantas unidades, faturamento total."

**Pergunta crítica:** "Qual a média de vendas?" → Soma dos valores ÷ quantidade de meses.

**Conexão identificada:** Venda **aponta para** produto do catálogo (para saber o que foi vendido) e **pertence a** usuário.

---

## Passo 2: O Teste da Frase "Pertence a"

Para cada classe, complete a frase:

| Classe                       | Completa a frase?                     | Resultado        |
| ---------------------------- | ------------------------------------- | ---------------- |
| Catálogo                     | "Catálogo pertence a **um** usuário"  | Sim → Composição |
| Despesa                      | "Despesa pertence a **um** usuário"   | Sim → Composição |
| Histórico                    | "Histórico pertence a **um** usuário" | Sim → Composição |
| Produto (dentro do catálogo) | "Produto pertence a **um** catálogo"  | Sim → Composição |

---

## Passo 3: O Teste "Sabe sobre" vs "Faz com"

| Classe    | Sabe sobre...        | Faz com...                                         |
| --------- | -------------------- | -------------------------------------------------- |
| Usuário   | Seus dados pessoais  | Coordena as outras classes                         |
| Catálogo  | Produtos disponíveis | Calcula lucro unitário                             |
| Despesa   | Contas do mês        | Calcula total a pagar                              |
| Histórico | Vendas passadas      | **Calcula média mensal** ← Seu objetivo principal! |

**Descoberta:** O cálculo da média está no **Histórico**, mas precisa de dados do **Catálogo** (preços) e **Despesa** (meta a atingir).

---

## Passo 4: Visualizando as Conexões (Mentalmente)

```
MENU FRONT (pergunta)
    │
    └──► USUÁRIO (coordena)
            │
            ├──► CATÁLOGO ◄──────┐
            │      │             │
            │      └── Produto 1─┘
            │          Produto 2    (Venda aponta para cá)
            │
            ├──► DESPESAS (lista de contas)
            │
            └──► HISTÓRICO DE VENDAS (lista de registros)
                       │
                       └── Cada venda: "Em fev/2024 vendi 50 unidades
                           do Produto 1, faturei R$1.750"
```

**Seta sólida (◆):** "Possui" / "É dono de"
**Seta tracejada (-->):** "Usa" / "Referencia"

---

## Passo 5: O Fluxo do Seu Objetivo Principal

**Objetivo:** "Média do valor dos produtos vendidos no mês"

**Caminho mental:**

1. Menu pergunta ao **Histórico**: "Qual sua média?"
2. Histórico olha seus registros: "Em jan: R$2.000, fev: R$3.000, mar: R$2.500..."
3. Histórico calcula: "(2000 + 3000 + 2500) ÷ 3 = R$2.500 média"
4. Histórico pergunta ao **Usuário**: "Quanto preciso cobrir?"
5. Usuário pergunta a **Despesas**: "Total do mês?"
6. Despesas responde: "R$2.000"
7. Usuário compara: "Média R$2.500 > Despesas R$2.000 = **Lucro de R$500**"
8. Resposta volta ao Menu: "Sua média cobre as despesas com sobra de R$500"

---

## 🎯 Exercício para Mudar sua Forma de Pensar

Pegue qualquer objeto físico na sua mesa. Pergunte:

| Pergunta                    | Exemplo: Caneta                  |
| --------------------------- | -------------------------------- |
| O que você **é**?           | Objeto de escrita                |
| O que você **sabe**?        | Cor da tinta, espessura da ponta |
| O que você **faz**?         | Escreve, desenha                 |
| A quem você **pertence**?   | A mim (está na minha mesa)       |
| Com quem você **interage**? | Papel, caderno, mão              |

**Aplique isso para cada classe do seu sistema.** A conexão aparece naturalmente quando você sabe "a quem pertence" e "com quem interage".

---

## ❓ Pergunta de Validação

Tente responder sem olhar nada:

> "Se eu deletar o Usuário, o que acontece com o Histórico de Vendas dele?"

- Se respondeu "some junto" → Você entendeu composição
- Se respondeu "fica no sistema" → Você está pensando em agregação (errado para este caso)

Qual foi sua resposta? Isso vai confirmar se a conexão ficou clara.
