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
    print("║ 3 - Buscar por Id             ║")  
    print("╚═══════════════════════════════╝")
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            print("Pedidos")
        case 2:
            print("Entregadores")
        case _:
            print("Opção inválida!") 

while True:
    print("\n╔═══════════════════════════════╗") 
    print("║             Menu              ║") 
    print("║ 1 - Pedidos                   ║") 
    print("║ 2 - Entregadores              ║") 
    print("║ 3 - Finalizar Sistema         ║") 
    print("╚═══════════════════════════════╝")
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            menu_pedidos()
        case 2:
            print("Entregadores")
        case _:
            print("Opção inválida!")
