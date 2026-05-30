from funcoes import *
import os


def menu_atualizacao_pedidos():

    while True:

        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║      ATUALIZACAO PEDIDOS     ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Alterar Status           ║")
        print("║ 2 - Cancelar Pedido          ║")
        print("║ 3 - Associar Entregador      ║")
        print("║ 4 - Remover Associacao       ║")
        print("║ 5 - Retornar                 ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opcao: "))
        except ValueError:
            print("\nDigite apenas numeros!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                alterar_status_pedido()
                input("\nPressione ENTER para continuar...")

            case 2:
                cancelar_pedido()
                input("\nPressione ENTER para continuar...")

            case 3:
                associar_entregador_pedido()
                input("\nPressione ENTER para continuar...")

            case 4:
                remover_associacao_entregador()
                input("\nPressione ENTER para continuar...")

            case 5:
                break

            case _:
                print("Opcao invalida!")
                input("\nPressione ENTER para continuar...")


def menu_pedidos():

    while True:

        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║            PEDIDOS           ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Cadastro                 ║")
        print("║ 2 - Atualizacao              ║")
        print("║ 3 - Pedidos Pendentes        ║")
        print("║ 4 - Pedidos Entregues        ║")
        print("║ 5 - Buscar por ID            ║")
        print("║ 6 - Retornar                 ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opcao: "))

        except ValueError:
            print("\nDigite apenas numeros!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                cadastrar_pedido()
                input("\nPressione ENTER para continuar...")

            case 2:
                menu_atualizacao_pedidos()

            case 3:
                listar_pedidos_pendentes()
                input("\nPressione ENTER para continuar...")

            case 4:
                listar_pedidos_entregues()
                input("\nPressione ENTER para continuar...")

            case 5:
                buscar_pedido_por_id()
                input("\nPressione ENTER para continuar...")

            case 6:
                break

            case _:
                print("Opcao invalida!")
                input("\nPressione ENTER para continuar...")


def menu_entregadores():

    while True:

        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║         ENTREGADORES         ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Cadastro                 ║")
        print("║ 2 - Entregas por Entregador  ║")
        print("║ 3 - Entregador Disponivel    ║")
        print("║ 4 - Retornar                 ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opcao: "))

        except ValueError:
            print("\nDigite apenas numeros!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                cadastrar_entregador()
                input("\nPressione ENTER para continuar...")

            case 2:
                listar_entregas_por_entregador()
                input("\nPressione ENTER para continuar...")

            case 3:
                buscar_entregador_disponivel()
                input("\nPressione ENTER para continuar...")

            case 4:
                return

            case _:
                print("Opcao invalida!")
                input("\nPressione ENTER para continuar...")


def menu_consultas():

    while True:

        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║           CONSULTAS            ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Pedidos Pendentes         ║")
        print("║ 2 - Pedidos Entregues         ║")
        print("║ 3 - Buscar Pedido por ID      ║")
        print("║ 4 - Entregador Disponivel     ║")
        print("║ 5 - Entregas por Entregador   ║")
        print("║ 6 - Retornar                  ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opcao: "))
        except ValueError:
            print("\nDigite apenas numeros!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                listar_pedidos_pendentes()
                input("\nPressione ENTER para continuar...")

            case 2:
                listar_pedidos_entregues()
                input("\nPressione ENTER para continuar...")

            case 3:
                buscar_pedido_por_id()
                input("\nPressione ENTER para continuar...")

            case 4:
                buscar_entregador_disponivel()
                input("\nPressione ENTER para continuar...")

            case 5:
                listar_entregas_por_entregador()
                input("\nPressione ENTER para continuar...")

            case 6:
                return

            case _:
                print("Opcao invalida!")
                input("\nPressione ENTER para continuar...")


def menu_relatorios():
    while True:
        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║          RELATORIOS          ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Relatorio de Pedidos     ║")
        print("║ 2 - Relatorio de Entregadores║")
        print("║ 3 - Relatorio Completo       ║")
        print("║ 4 - Retornar                 ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opcao: "))
        except ValueError:
            print("\nDigite apenas numeros!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                gerar_relatorio_pedidos()
                input("\nPressione ENTER para continuar...")
            case 2:
                gerar_relatorio_entregadores()
                input("\nPressione ENTER para continuar...")
            case 3:
                gerar_relatorio_completo()
                input("\nPressione ENTER para continuar...")
            case 4:
                return
            case _:
                print("Opcao invalida!")
                input("\nPressione ENTER para continuar...")


while True:

    os.system("cls")

    print("\n╔═══════════════════════════════╗")
    print("║              MENU            ║")
    print("╠═══════════════════════════════╣")
    print("║ 1 - Pedidos                  ║")
    print("║ 2 - Entregadores             ║")
    print("║ 3 - Consultas                ║")
    print("║ 4 - Relatorios               ║")
    print("║ 5 - Finalizar Sistema        ║")
    print("╚═══════════════════════════════╝")

    try:
        opcao = int(input("Opcao: "))

    except ValueError:
        print("\nDigite apenas numeros!")
        input("\nPressione ENTER para continuar...")
        continue

    match opcao:

        case 1:
            menu_pedidos()

        case 2:
            menu_entregadores()

        case 3:
            menu_consultas()

        case 4:
            menu_relatorios()

        case 5:
            os.system("cls")
            print("Sistema finalizado!")
            break

        case _:
            print("\nOpcao invalida!")
            input("\nPressione ENTER para continuar...")
