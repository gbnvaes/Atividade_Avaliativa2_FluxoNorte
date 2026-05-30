## Cadastro de pedidos
pedido = {}
def validar_id_pedido(id_pedido):   
    return len(id_pedido) ==5 and id_pedido[0].isalpha() and id_pedido[1].isdigit()

def cadastrar_pedido():
    print("\n--- CADASTRO DO PEDIDO ---\n")

    id_pedido = input("ID do pedido: ")
    while not validar_id_pedido(id_pedido):
        print("ID do pedido esta invalido. Tente novamente!!")
        id_pedido = input("ID do pedido: ")

    nome_cliente = input("Digite o nome do cliente: ")
    while not nome_cliente.replace(" ", "").isalpha():
        print("Nome inválido! Digite apenas letras.")
        nome_cliente = input("Digite o nome do cliente: ")

    endereco = input("Digite o enderço da entrega: ")

    prioridade = input("Digite a prioridade do seu pedido (NORMAL/ALTA):").upper()
    while prioridade not in ["ALTA", "NORMAL"]:
        print("Propriedade invalida. Digite se é de prioridade (NORMAL/ALTA)")
        prioridade = input("Digite a prioridade do seu pedido (NORMAL/ALTA):").upper()

    descricao_pedido = str(input("Faça a descrição do pedido: "))
    while len(descricao_pedido) < 5:
        print("Escreva a descrição do pedido realizado!")
        descricao_pedido = str(input("Faça a descrição do pedido: "))

    status_opcoes = ["Pendente", "Em Rota", "Entregue", "Cancelado"]
    print("Status disponíveis: Pendente, Em Rota, Entregue, Cancelado")
    status = input("Digite o status do pedido: ").title().strip()
    while status not in status_opcoes:
        print("Status invalido!! Escoleha entre: Pendente, Em Rota, Entregue, Cancelado .")
        status = input("Digite o status do pedido: ").title().strip()

    id_entregador = input("Digite o ID do entregador: ")
    while len(id_entregador) != 4 or not id_entregador.isdigit():
        print("ID do entregador esta incorreto!! Tente novamente.")
        id_entregador = input("Digite o ID do entregador: ")

    pedido[id_pedido] = [
        nome_cliente,
        endereco,
        prioridade,
        descricao_pedido,
        status,
        id_entregador
    ]

    print("\n=== Pedido Cadastrado com Sucesso! ===")

    # Exibe o dicionário com os dados do pedido
    campos = ["Nome do cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID do entregador"]
    print(f"\nPedido ID: {id_pedido}")
    for campo, valor in zip(campos, pedido[id_pedido]):
        print(f"  {campo}: {valor}")

    

entregadores = {}

def cadastrar_entregador():
    print("\n--- CADASTRO DE ENTREGADOR ---\n")
 
    id_entregador = input("ID Entregador: ")

    while len(id_entregador) != 4 or not id_entregador.isdigit() or id_entregador in entregadores:
        print("ID inválido!")
        if id_entregador in entregadores:
            print("Esse ID já está cadastrado!")

        id_entregador = input("ID Entregador: ")

    nome = input("Nome: ")

    while not nome.replace(" ", "").isalpha():
        print("Nome inválido! Digite apenas letras.")
        nome = input("Nome: ")

    veiculo = input("Veículo [Carro | Moto | Van]: ").title()

    while veiculo not in ["Carro", "Moto", "Van"]:
        print("Veículo inválido!")
        veiculo = input("Veículo [Carro | Moto | Van]: ").title()
  
    id_pedido = input("ID do Pedido: ")

  
    disponibilidade = input("Disponibilidade [Disponível/Indisponível]: ").title()

    while disponibilidade not in ["Disponível", "Indisponível"]:
        print("Digite apenas Disponível ou Indisponível.")
        disponibilidade = input("Disponibilidade: ").title()

    entregadores[id_entregador] = [
        nome,
        veiculo,
        id_pedido,
        disponibilidade
    ]
    return entregadores
    print("\n=== ENTREGADOR CADASTRADO COM SUCESSO ===")

##Atualizar status do pedido

def alterar_status_pedido():
    print("\n--- ALTERAR STATUS DO PEDIDO ---\n")

    id_pedido = input("Digite o id do pedido: ")

    if id_pedido in pedido:
        print(f"Status atual: {pedido[id_pedido[4]]}")

        status_opcoes = ["Pendente", "Em Rota", "Entregue", "Cancelado"]
        print(f"Status disponiveis:{status_opcoes}")

        novo_status = input("Digite o novo status do seu pedido:").upper().strip()
        while novo_status not in status_opcoes:
            print(f"Status invalidio. Os status diponiveis são:{status_opcoes}")
            novo_status = input("Digite o novo status: ").upper().strip()

        pedido[id_pedido][4] = novo_status
        print(f"\nStatus do pedido atualizado com sucesso! Novo status: {novo_status}")
    else:
        print("Pedido não encontrado")    