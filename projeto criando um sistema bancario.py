#esafio: um sistema bancario com as operações: depositar, sacar e visualizar extrato
texto="Por Favor escolha uma opção abaixo:"
print(texto.title())
menu = """
[D]Depositar
[S]Sacar
[E]Extrato
[Q]Sair
"""

#Operação de deposito:todos os depositos devem ser armazenados em uma variavel e exibidos na operaçao de extrato
#Operação de saque:o sistema deve permitir apenas 3 saques diarios com no maximo 500R$ por saque, o sistema deve iformar por msg "que nao e possivel sacar o dinheiro por falta de saldo
saldo=0
limite=500
extrato=''
saques_diarios=0
LIMITE_SAQUE=3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("valor depositado!\nEscolha novamente uma opção")
            
        else:
            print("operação falhou valor informado e inválido.")
    
    elif opcao == "s":
        valor=float(input("informe o valor do saque:"))
        
        excedeu_limite= valor>valor
        excedeu_saque=saques_diarios>LIMITE_SAQUE
        excedeu_saldo= valor>saldo
        if excedeu_saldo:
            print("voce nao tem saldo suficiente.\nescolha novamente uma opção.")
        elif excedeu_saque:
            print("você utilizou todos os saques diarios.")
        elif valor > 0:
            saldo -= valor
            extrato +=f'saque: R${valor:.2f}\n'
            saques_diarios +=1
            print("saque realizado com sucesso!")
        else:
            print("operação falhou, o valor informado esta errado.")
    elif opcao== "e":
        print("\n============extrato============")
        print("não fpra realizadas movimentações.")
        print(f"\n extrato:{extrato:}")
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=================================")
    elif opcao== "q":
        print("obrigado, tenha um bom dia!")
        break
    else:
        print("não indentificamos sua operação, por favor informe ua nova opção.")
        
        






# todos os saques devem ser armazenados em uma variavel e exibido na opção de extrato
#operação de extrato:esta operação deve listar toos os depositos e saque realizados na conta,se o extrato estivar em branco exibir a msg: não foram realizadas mivimentações
#os valores devem ser exibidos usando o formato R$xxx.xx ex: 1500.45= 1500.45