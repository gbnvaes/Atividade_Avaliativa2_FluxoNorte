pedidos = []

def validar_id_pedido(id_pedido):   
    return len(id_pedido) ==5 and id_pedido[0].isalpha() and id_pedido[1].isdigit()

def cadastrar_pedido():
    print("\n--- CADASTRO DO PEDIDO ---\n")

    id_pedido = input("ID do pedido: ")#AUTORIZAÇÃO DO ID
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

    pedido = {
        "id_pedido": id_pedido,
        "nome_cliente": nome_cliente,
        "endereco": endereco,
        "prioridade": prioridade,
        "descricao": descricao_pedido,
        "status": status,
        "id_entregador": id_entregador
    }

    pedidos.append(pedido)

    print("\n=== Pedido Cadastrado com Sucesso! ===")
    print(f"ID do Pedido:     {id_pedido}")
    print(f"Cliente:          {nome_cliente}")
    print(f"Endereço:         {endereco}")
    print(f"Prioridade:       {prioridade}")
    print(f"Descrição:        {descricao_pedido}")
    print(f"Status:           {status}")
    print(f"ID do Entregador: {id_entregador}")


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


    