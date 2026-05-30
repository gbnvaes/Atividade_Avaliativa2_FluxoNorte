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
    if id_pedido in pedido:
        print("Esse ID de pedido já está cadastrado!")
        return

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

    
    campos = ["Nome do cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID do entregador"]
    print(f"\nPedido ID: {id_pedido}")
    for campo, valor in zip(campos, pedido[id_pedido]):
        print(f"  {campo}: {valor}")

    

entregadores = {}

def cadastrar_entregador():
    print("\n--- CADASTRO DE ENTREGADOR ---\n")
 
    id_entregador = input("ID Entregador: ")

    while len(id_entregador) != 4 or not id_entregador.isdigit() or id_entregador in entregadores:
        if id_entregador in entregadores:
            print("Esse ID já está cadastrado!")
        else:
            print("ID inválido! O ID deve ter 4 dígitos numéricos.")
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
    
    print("\n=== ENTREGADOR CADASTRADO COM SUCESSO ===")
    campos = ["Nome", "Veículo", "ID do Pedido", "Disponibilidade"]
    print(f"\nEntregador ID: {id_entregador}")

    for campo, valor in zip(campos, entregadores[id_entregador]):
        print(f"  {campo}: {valor}")

    return entregadores

## Atualizar status do pedido

def alterar_status_pedido():
    print("\n--- ALTERAR STATUS DO PEDIDO ---\n")

    if not pedido:
        print("Nenhum pedido cadastrado!")
        return

    id_pedido = input("Digite o id do pedido: ")

    if id_pedido in pedido:
        status_opcoes = ["Pendente", "Em Rota", "Entregue", "Cancelado"]
        print(f"Status atual: {pedido[id_pedido[4]]}")
        print(f"Status disponíveis: {', '.join(status_opcoes)}")

        novo_status = input("Digite o novo status do seu pedido:").upper().strip()
        while novo_status not in status_opcoes:
            print(f"Status invalidio. Os status diponiveis são:{status_opcoes}")
            novo_status = input("Digite o novo status: ").upper().strip()

        pedido[id_pedido][4] = novo_status
        print(f"\nStatus do pedido atualizado com sucesso! Novo status: {novo_status}")
    else:
        print("Pedido não encontrado")    

## Listar pedidos pendentes
def listar_pedidos_pendentes():
    print("\n--- PEDIDOS PENDENTES ---\n")
 
    pendentes = []
    for id_p, dados in pedido.items():
        if dados[4] == "Pendente":
            pendentes.append(id_p)
 
    if len(pendentes) == 0:
        print("Nenhum pedido pendente no momento.")
        return
 
    campos = ["Nome do cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID do entregador"]
    print(f"Total de pedidos pendentes: {len(pendentes)}\n")
    print("-" * 45)
 
    for id_p in pendentes:
        print(f"Pedido ID: {id_p}")
        for campo, valor in zip(campos, pedido[id_p]):
            print(f"  {campo}: {valor}")
        print("-" * 45)
 
 
## Listar pedidos entregues
def listar_pedidos_entregues():
    print("\n--- PEDIDOS ENTREGUES ---\n")
 
    entregues = []
    for id_p, dados in pedido.items():
        if dados[4] == "Entregue":
            entregues.append(id_p)
 
    if len(entregues) == 0:
        print("Nenhum pedido entregue no momento.")
        return
 
    campos = ["Nome do cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID do entregador"]
    print(f"Total de pedidos entregues: {len(entregues)}\n")
    print("-" * 45)
 
    for id_p in entregues:
        print(f"Pedido ID: {id_p}")
        for campo, valor in zip(campos, pedido[id_p]):
            print(f"  {campo}: {valor}")
        print("-" * 45)
 
 
## Buscar pedido por ID
def buscar_pedido_por_id():
    print("\n--- BUSCAR PEDIDO POR ID ---\n")
 
    if not pedido:
        print("Nenhum pedido cadastrado!")
        return
 
    id_busca = input("Digite o ID do pedido: ")
 
    if id_busca in pedido:
        campos = ["Nome do cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID do entregador"]
        print(f"\nPedido encontrado!")
        print("-" * 45)
        print(f"Pedido ID: {id_busca}")
        for campo, valor in zip(campos, pedido[id_busca]):
            print(f"  {campo}: {valor}")
        print("-" * 45)
    else:
        print(f"Pedido com ID '{id_busca}' não encontrado!")
 
 
## Entregas por entregador
def listar_entregas_por_entregador():
    print("\n--- ENTREGAS POR ENTREGADOR ---\n")
 
    if not entregadores:
        print("Nenhum entregador cadastrado!")
        return
 
    id_busca = input("Digite o ID do entregador: ")
 
    if id_busca not in entregadores:
        print(f"Entregador com ID '{id_busca}' não encontrado!")
        return
 
    nome_entregador = entregadores[id_busca][0]
    print(f"\nEntregador: {nome_entregador} (ID: {id_busca})")
    print("-" * 45)
 
    pedidos_entregador = []
    for id_p, dados in pedido.items():
        if dados[5] == id_busca:
            pedidos_entregador.append(id_p)
 
    if len(pedidos_entregador) == 0:
        print("Nenhum pedido vinculado a este entregador.")
        return
 
    campos = ["Nome do cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID do entregador"]
    print(f"Total de pedidos: {len(pedidos_entregador)}\n")
 
    for id_p in pedidos_entregador:
        print(f"  Pedido ID: {id_p}")
        for campo, valor in zip(campos, pedido[id_p]):
            print(f"    {campo}: {valor}")
        print()
 
 ## Gerar relatórios
def gerar_relatorio_pedidos():
    print("\n" + "=" * 50)
    print("         RELATÓRIO GERAL DE PEDIDOS")
    print("=" * 50)
 
    if not pedido:
        print("\nNenhum pedido cadastrado no sistema.")
        return
 
    contagem_status = {
        "Pendente": 0,
        "Em Rota": 0,
        "Entregue": 0,
        "Cancelado": 0
    }
 
    contagem_prioridade = {
        "ALTA": 0,
        "NORMAL": 0
    }
 
    for id_p, dados in pedido.items():
        status_atual = dados[4]
        prioridade_atual = dados[2]
 
        if status_atual in contagem_status:
            contagem_status[status_atual] = contagem_status[status_atual] + 1
 
        if prioridade_atual in contagem_prioridade:
            contagem_prioridade[prioridade_atual] = contagem_prioridade[prioridade_atual] + 1
 
    total = len(pedido)
    print(f"\n  Total de pedidos cadastrados: {total}")
    print("\n  --- Pedidos por Status ---")
    for status, qtd in contagem_status.items():
        print(f"    {status}: {qtd}")
 
    print("\n  --- Pedidos por Prioridade ---")
    for prio, qtd in contagem_prioridade.items():
        print(f"    {prio}: {qtd}")
 
    print("\n  --- Listagem Completa ---")
    print("  " + "-" * 46)
 
    campos = ["Cliente", "Endereço", "Prioridade", "Descrição", "Status", "ID Entregador"]
    for id_p, dados in pedido.items():
        print(f"  Pedido: {id_p}")
        for campo, valor in zip(campos, dados):
            print(f"    {campo}: {valor}")
        print("  " + "-" * 46)
 
    print("=" * 50)
 
 
def gerar_relatorio_entregadores():
    print("\n" + "=" * 50)
    print("       RELATÓRIO GERAL DE ENTREGADORES")
    print("=" * 50)
 
    if not entregadores:
        print("\nNenhum entregador cadastrado no sistema.")
        return
 
    contagem_veiculo = {
        "Carro": 0,
        "Moto": 0,
        "Van": 0
    }
 
    contagem_disponibilidade = {
        "Disponível": 0,
        "Indisponível": 0
    }
 
    for id_e, dados in entregadores.items():
        veiculo_atual = dados[1]
        disp_atual = dados[3]
 
        if veiculo_atual in contagem_veiculo:
            contagem_veiculo[veiculo_atual] = contagem_veiculo[veiculo_atual] + 1
 
        if disp_atual in contagem_disponibilidade:
            contagem_disponibilidade[disp_atual] = contagem_disponibilidade[disp_atual] + 1
 
    total = len(entregadores)
    print(f"\n  Total de entregadores cadastrados: {total}")
 
    print("\n  --- Por Tipo de Veículo ---")
    for veiculo, qtd in contagem_veiculo.items():
        print(f"    {veiculo}: {qtd}")
 
    print("\n  --- Por Disponibilidade ---")
    for disp, qtd in contagem_disponibilidade.items():
        print(f"    {disp}: {qtd}")
 
    print("\n  --- Listagem Completa ---")
    print("  " + "-" * 46)
 
    campos_e = ["Nome", "Veículo", "ID Pedido", "Disponibilidade"]
    for id_e, dados in entregadores.items():
        print(f"  Entregador ID: {id_e}")
        # Conta pedidos vinculados ao entregador
        pedidos_vinculados = []
        for id_p, dp in pedido.items():
            if dp[5] == id_e:
                pedidos_vinculados.append(id_p)
        for campo, valor in zip(campos_e, dados):
            print(f"    {campo}: {valor}")
        print(f"    Pedidos vinculados: {len(pedidos_vinculados)}")
        print("  " + "-" * 46)
 
    print("=" * 50)
 
 
def gerar_relatorio_completo():
    print("\n" + "=" * 50)
    print("         RELATÓRIO COMPLETO DO SISTEMA")
    print("=" * 50)
 
    resumo = [
        ["Total de Pedidos", len(pedido)],
        ["Total de Entregadores", len(entregadores)]
    ]
 
    pendentes = 0
    em_rota = 0
    entregues = 0
    cancelados = 0
 
    for id_p, dados in pedido.items():
        if dados[4] == "Pendente":
            pendentes = pendentes + 1
        elif dados[4] == "Em Rota":
            em_rota = em_rota + 1
        elif dados[4] == "Entregue":
            entregues = entregues + 1
        elif dados[4] == "Cancelado":
            cancelados = cancelados + 1
 
    resumo.append(["  - Pendentes", pendentes])
    resumo.append(["  - Em Rota", em_rota])
    resumo.append(["  - Entregues", entregues])
    resumo.append(["  - Cancelados", cancelados])
 
    disponiveis = 0
    indisponiveis = 0
    for id_e, dados in entregadores.items():
        if dados[3] == "Disponível":
            disponiveis = disponiveis + 1
        else:
            indisponiveis = indisponiveis + 1
 
    resumo.append(["  - Entregadores Disponíveis", disponiveis])
    resumo.append(["  - Entregadores Indisponíveis", indisponiveis])
 
    print()
    for item in resumo:
        rotulo = item[0]
        valor = item[1]
        print(f"  {rotulo}: {valor}")
 
    print("\n" + "=" * 50)