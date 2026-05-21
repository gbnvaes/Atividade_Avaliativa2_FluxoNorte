from funcoes import *
import os
def menu_pedidos():
    os.system("cls")
    print("\n╔═══════════════════════════════╗") 
    print("║             Pedidos           ║") 
    print("║ 1 - Cadastro                  ║") 
    print("║ 2 - Atualização               ║") 
    print("║ 3 - Pedidos pendentes         ║") 
    print("║ 4 - Pedidos entregues         ║")
    print("║ 5 - Buscar por Id             ║")  
    print("║ 6 - Retornar                  ║")  
    print("╚═══════════════════════════════╝")
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            print("cadastro")
        case 2:
            print("Atualização")
        case 3:
            print("Pedidos Pendentes")
        case 4:
            print("Pedidos Entregues")
        case 5:
            print("Buscar por Id")
        case 6:
            return
        case _:
            print("Opção inválida!") 




def menu_entregadores():
    os.system("cls")
    print("\n╔═══════════════════════════════╗") 
    print("║          Entregadores         ║") 
    print("║ 1 - Cadastro                  ║") 
    print("║ 2 - Atualização               ║") 
    print("║ 3 - Entregas por entregador   ║")
    print("║ 4 - Retornar                  ║")  
    print("╚═══════════════════════════════╝")
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            print("Pedidos")
        case 2:
            print("Entregadores")
        case 3:
            print("Entregadores")
        case _:
            print("Opção inválida!") 



opcao = 1
while opcao != 5:
    print("\n╔═══════════════════════════════╗") 
    print("║             Menu              ║") 
    print("║ 1 - Pedidos                   ║") 
    print("║ 2 - Entregadores              ║") 
    print("║ 3 - consultas                 ║") 
    print("║ 4 - Relatorios                ║") 
    print("║ 5 - Finalizar Sistema         ║") 
    print("╚═══════════════════════════════╝")
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            menu_pedidos()
        case 2:
            menu_entregadores()
        case 3:
            print("consultas")
        case 4:
            print("Relatorios")
        case 5:
            print("Sistema finalizado")
        case _:
            print("Opção inválida!")
