import textwrap
def menu():
    menu="""
    ==========MENU==========
    [d]Depositar
    [s]Saque
    [e]Extrato
    [nc]Nova Conta
    [lc]Listar contas
    [nu]Novo Usuário    
    [q]Sair
=>"""
    return input(textwrap.dedent(menu))
def main():
    usuarios= []
    contas=[]
    saldo= 0
    limite= 500
    extrato= ""
    valor= float
    numeros_saques= 0
    LIMITE_SAQUE= 3
    AGENCIA="0001"
    while True:
        opcao=menu()
        if opcao =="d":
            valor=float(input("Informe o valor que deseja depositar: "))
            saldo, extrato= depositar(saldo, valor, extrato)
        elif opcao=="s":
            valor=float(input("Informe o valor que deseja sacar: "))
            saldo, extrato= sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limite_saques=LIMITE_SAQUE,
            )
        elif opcao=="e":
            print(f"Saldo:\t\tR${saldo:.2f}")

            exibir_extrato(saldo, extrato=extrato)
        elif opcao=="nu":
            criar_usuario(usuarios)
        elif opcao=="nc":
            numero_conta= len(contas)+ 1
            conta= criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao=="lc":
            listar_contas(contas)
def depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo+=valor
        extrato+=f"Deposito: R${valor:.2f}\n"
        print("\n===Deposito realizado com sucesso! ===")
    else:
        print("@@@Operação falhou!O valor informado é inválido. @@@")
    return saldo, extrato
def sacar(*,saldo, valor, extrato, limite, numeros_saques, limite_saques):
        excedeu_saldo= valor>saldo
        excedeu_limite= valor>limite
        excedeu_saques= numeros_saques>=limite_saques
        if excedeu_saldo:
           print("Operação falhou! Você não tem saldo o suficiente.") 
        elif excedeu_limite:
            print("Operação falhou!O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou!Número maximo de saques excedido.")
        elif valor>0:
            saldo-=valor
            extrato+= f"Saque R$: {valor:.2f}\n"
            numeros_saques+=1
            print("\n===Saque realizado com sucesso!===")
        else:
            print("Operação falhou!O valor informado é inválido.")
        return saldo, extrato
def exibir_extrato(saldo, /,*, extrato):
        print("==========Extrato==========")
        print("Não foram realizadas movimentações"if not extrato else extrato)
        print(f"Saldo:\t\tR${saldo:.2f}")
        print("==============================")
def criar_usuario(usuarios):
    cpf= input("Me informe o seu CPF(Apenas os números): ")
    usuario= filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF informado! @@@ ")
        return
    nome= input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe o seu endereço: ")
    usuarios.append({"nome": nome,"data_nascimento": data_nascimento,"cpf": cpf,"endereco": endereco})
    print("===Usuário criado com sucesso!===")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados= [usuarios for usuarios in usuarios if usuarios["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf= input("Informe o CPF do usuário: ")
    usuario= filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrada @@@")
def listar_contas(contas):
    for conta in contas:
        linha= f"""\
        Agência:\t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
    """  
    print("="*100)
    print(textwrap.dedent(linha))
main()