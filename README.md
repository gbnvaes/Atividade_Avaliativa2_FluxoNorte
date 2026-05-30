# 📦 FluxoNorte — Sistema de Controle de Entregas

Sistema operacional em Python para gerenciamento de pedidos e entregadores da empresa de logística urbana **FluxoNorte**. Desenvolvido como Atividade Avaliativa A2 da disciplina de Algoritmos de Programação.

---

## 📋 Sobre o Projeto

A FluxoNorte enfrentava problemas recorrentes no controle de distribuição de entregas: registros manuais, dados espalhados em planilhas e informações desatualizadas. Este sistema foi desenvolvido para centralizar e organizar as operações diárias da empresa, permitindo cadastro, atualização e consulta de pedidos e entregadores de forma estruturada, sem o uso de banco de dados ou interfaces gráficas — todos os dados são mantidos em memória utilizando estruturas nativas do Python.

---

## 🗂️ Estrutura de Arquivos

```
├── menu.py       # Ponto de entrada do sistema — menus de navegação
├── funcoes.py    # Funções de cadastro, validação e manipulação de dados
└── README.md
```

---

## ⚙️ Funcionalidades

### Pedidos
- Cadastro de pedidos com validação de todos os campos
- Atualização de status (Pendente → Em Rota → Entregue / Cancelado)
- Cancelamento de pedido e remoção de associação com entregador
- Listagem de pedidos pendentes e entregues
- Busca por ID

### Entregadores
- Cadastro de entregadores sem duplicidade de ID
- Associação de pedidos a entregadores
- Consulta de disponibilidade
- Listagem de todas as entregas realizadas por um entregador

### Relatórios Operacionais
- Total de pedidos cadastrados
- Quantidade de pedidos por status
- Pedidos com prioridade Alta
- Entregador com maior número de entregas

---

## 🔐 Regras de Validação

| Campo | Regra |
|---|---|
| ID do Pedido | 1 letra + 4 dígitos (ex: `A1234`) |
| ID do Entregador | Exatamente 4 dígitos (ex: `0042`) |
| Nome | Somente letras e espaços |
| Prioridade | `NORMAL` ou `ALTA` |
| Status | `Pendente`, `Em Rota`, `Entregue` ou `Cancelado` |
| Veículo | `Carro`, `Moto` ou `Van` |
| Disponibilidade | `Disponível` ou `Indisponível` |
| Descrição | Mínimo de 5 caracteres |

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.10 ou superior (necessário para o uso de `match/case`).

```bash
python menu.py
```

Compatível com **IDLE do Python.org** e **VS Code**.

> O sistema utiliza `os.system("cls")` para limpar o terminal — compatível com Windows. Em sistemas Linux/macOS, substitua por `os.system("clear")`.

---

## 🧱 Estruturas de Dados

Os dados são armazenados em dicionários Python em memória durante a execução:

```python
# Pedidos — chave: ID do pedido
pedido = {
    "A1234": ["Nome Cliente", "Endereço", "ALTA", "Descrição", "Pendente", "0042"]
}

# Entregadores — chave: ID do entregador
entregadores = {
    "0042": ["Nome", "Moto", "A1234", "Disponível"]
}
```

> ⚠️ Por se tratar de armazenamento em memória, os dados **não são persistidos** entre execuções do sistema.

---

