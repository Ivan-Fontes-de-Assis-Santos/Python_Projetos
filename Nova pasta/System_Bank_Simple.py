#Declaração de variável e constantes!
menu="""
[d] Depositar
[s] Saque
[e] Extrato
[q] Sair
=> """

saldo= 0
limite= 500
extrato= ""
numeros_saques= 0
LIMITE_SAQUE= 3
valor= float
#Ultilizei o while para repetir enquanto a solicitção for válida ele continuar repetindo!
while True:
    #Início do código:
    opcao= input(menu)
    #Condicional se a opção for "D":
    if opcao == "d":
        valor= float(input("Informe o valor que deseja depositar: "))
        #Adiciona o valor informado no saldo e no extrato:
        if valor > 0:
            saldo += valor        
            extrato += f"Deposito R$: {valor:.2f}\n "
        #Caso o valor informado for inválido, esse código será executado:
        else:
            print("Operação falhou! O valor informado é inválido.")
    #Condicional se a opção for "S":
    elif opcao == "s":
        valor= float(input("Informe um valor que deseja sacar: "))
        #Declarando variáveis para a opção de saque:
        excedeu_saldo= valor>saldo
        excedeu_limite= valor>limite
        excedeu_saques= numeros_saques>=LIMITE_SAQUE
        #Se alguma variável acima não for executada corretamente, aparecerá os códigos abaixo na tela:
        if excedeu_saldo:
           print("Operação falhou! Você não tem saldo o suficiente.") 
        elif excedeu_limite:
            print("Operação falhou!O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou!Número maximo de saques excedido.")
        #Caso estiver certo, o valor informado será descontado do saldo; E aparecerá no extrato o saque realizado; E contabilizará +1 na variável número de saques.
        elif valor>0:
            saldo-=valor
            extrato+= f"Saque R$: {valor:.2f}\n"
            numeros_saques+=1
        #Caso o valor informado for inválido, esse código será executado:
        else:
            print("Operação falhou!O valor informado é inválido.")
    #Caso a opção seja "E", será executado esse código mostrando as movimentações bancárias:
    elif opcao=="e":
        print("/n==========Extrato==========")
        #Caso não tenha realizado nenhuma movimentação na conta, será executado essa condicional:
        print("Não foram realizadas movimentações"if not extrato else extrato)
        print(f"\nSaldo R$: {valor:.2f}")
        print("==============================")
    #Condicional para a opção "Q":  
    elif opcao=="q":    
        break
    else:
         print("Operação inválida, por favor selecione novamente a operação desejada.")
