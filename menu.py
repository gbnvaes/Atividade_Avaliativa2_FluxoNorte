from funcoes import *
import os



def menu_pedidos():

    while True:

        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║            PEDIDOS           ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Cadastro                 ║")
        print("║ 2 - Atualização              ║")
        print("║ 3 - Pedidos Pendentes        ║")
        print("║ 4 - Pedidos Entregues        ║")
        print("║ 5 - Buscar por ID            ║")
        print("║ 6 - Retornar                 ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opção: "))

        except ValueError:
            print("\nDigite apenas números!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                cadastrar_pedido()
                input("\nPressione ENTER para continuar...")

            case 2:
                print("Atualização")
                input("\nPressione ENTER para continuar...")

            case 3:
                print("Pedidos Pendentes")
                input("\nPressione ENTER para continuar...")

            case 4:
                print("Pedidos Entregues")
                input("\nPressione ENTER para continuar...")

            case 5:
                print("Buscar por ID")
                input("\nPressione ENTER para continuar...")

            case 6:
                break

            case _:
                print("Opção inválida!")
                input("\nPressione ENTER para continuar...")



def menu_entregadores():

    while True:

        os.system("cls")

        print("\n╔═══════════════════════════════╗")
        print("║         ENTREGADORES         ║")
        print("╠═══════════════════════════════╣")
        print("║ 1 - Cadastro                 ║")
        print("║ 2 - Entregas por Entregador  ║")
        print("║ 3 - Retornar                 ║")
        print("╚═══════════════════════════════╝")

        try:
            opcao = int(input("Opção: "))

        except ValueError:
            print("\nDigite apenas números!")
            input("\nPressione ENTER para continuar...")
            continue

        os.system("cls")

        match opcao:

            case 1:
                cadastrar_entregador()
                input("\nPressione ENTER para continuar...")

            case 2:
                print("Entregas")
            case 3:
                return

            case _:
                print("Opção inválida!")
                input("\nPressione ENTER para continuar...")



while True:

    os.system("cls")

    print("\n╔═══════════════════════════════╗")
    print("║              MENU            ║")
    print("╠═══════════════════════════════╣")
    print("║ 1 - Pedidos                  ║")
    print("║ 2 - Entregadores             ║")
    print("║ 3 - Consultas                ║")
    print("║ 4 - Relatórios               ║")
    print("║ 5 - Finalizar Sistema        ║")
    print("╚═══════════════════════════════╝")

    try:
        opcao = int(input("Opção: "))

    except ValueError:
        print("\nDigite apenas números!")
        input("\nPressione ENTER para continuar...")
        continue

    match opcao:

        case 1:
            menu_pedidos()

        case 2:
            menu_entregadores()

        case 3:
            print("\nConsultas")
            input("\nPressione ENTER para continuar...")

        case 4:
            print("\nRelatórios")
            input("\nPressione ENTER para continuar...")

        case 5:
            os.system("cls")
            print("Sistema finalizado!")
            break

        case _:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")