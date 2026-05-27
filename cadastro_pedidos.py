def validar_id_pedido(id_pedido):
    return len(id_pedido) ==5 and id_pedido[0].isalpha() and id_pedido[1].isdigit()

def casatrar_pedido():
    print("\n--- CASATRO DO PEDIDO ---\n")

    id_pedido = input("ID do pedido: ")#AUTORIZAÇÃO DO ID
    while not validar_id_pedido(id_pedido):
        print("ID do pedido esta invalido. Tente novamente!!")
        id_pedido = input("ID do pedido: ")

    nome_cliente = str(input("Digite o nome do cliente: "))

    endereco = input("Digite o enderço da entrega: ")

    prioridade = input("Digite a prioridade do seu pedido (NORMAL/ALTA):").upper
    if prioridade == alta:
       





