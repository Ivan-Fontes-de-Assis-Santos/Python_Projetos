from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Menu:
    def __init__(self):
        self.opcoes = {
            'd': "Depositar",
            's': "Saque",
            'e': "Extrato",
            'nc': "Nova Conta",
            'lc': "Listar contas",
            'nu': "Novo Usuário",
            'q': "Sair"
        }

    def mostrar_menu(self):
        menu_str = """
        ==========MENU==========
        [d] Depositar
        [s] Saque
        [e] Extrato
        [nc] Nova Conta
        [lc] Listar contas
        [nu] Novo Usuário    
        [q] Sair
        => """
        return input(textwrap.dedent(menu_str))

    def processar_escolha(self, escolha):
        escolha = escolha.lower()
        if escolha in self.opcoes:
            return escolha
        else:
            print("Opção inválida! Escolha uma opção válida.")
            return None
class Main:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.menu = Menu()

    def executar(self):
        while True:
            escolha = self.menu.mostrar_menu()
            if escolha:
                if escolha == 'q':
                    print("Saindo do programa...")
                    break
                elif escolha == 'nc':
                    self.criar_nova_conta()
                elif escolha == 'nu':
                    self.criar_novo_usuario()
                elif escolha == 'lc':
                    self.listar_contas()
                else:
                    self.processar_conta(escolha)
            else:
                print("Escolha inválida!")

    def criar_nova_conta(self):
        print("\n=== Criando nova conta ===")
        tipo_conta = input("Digite o tipo de conta (Corrente / Poupança): ").lower()
        if tipo_conta == 'corrente':
            self.criar_conta_corrente()
        elif tipo_conta == 'poupança':
            self.criar_conta_poupanca()
        else:
            print("Tipo de conta inválido!")

    def criar_conta_corrente(self):
        nome_titular = input("Digite o nome do titular: ")
        endereco = input("Digite o endereço do titular: ")
        cpf = input("Digite o CPF do titular: ")
        numero_conta = input("Digite o número da conta: ")
        cliente = PessoaFisica(endereco, nome_titular, datetime.now(), cpf)
        nova_conta = ContaCorrente(numero_conta, cliente)
        self.contas.append(nova_conta)
        cliente.adicionar_conta(nova_conta)
        print(f"\n=== Conta Corrente criada com sucesso para {nome_titular} ===")

    def criar_conta_poupanca(self):
        nome_titular = input("Digite o nome do titular: ")
        endereco = input("Digite o endereço do titular: ")
        cpf = input("Digite o CPF do titular: ")
        numero_conta = input("Digite o número da conta: ")
        cliente = PessoaFisica(endereco, nome_titular, datetime.now(), cpf)
        nova_conta = ContaPoupanca(numero_conta, cliente)
        self.contas.append(nova_conta)
        cliente.adicionar_conta(nova_conta)
        print(f"\n=== Conta Poupança criada com sucesso para {nome_titular} ===")

    def criar_novo_usuario(self):
        print("\n=== Criando novo usuário ===")
        tipo_usuario = input("Digite o tipo de usuário (Física / Jurídica): ").lower()
        if tipo_usuario == 'física':
            self.criar_usuario_fisica()
        elif tipo_usuario == 'jurídica':
            self.criar_usuario_juridica()
        else:
            print("Tipo de usuário inválido!")

    def criar_usuario_fisica(self):
        nome = input("Digite o nome completo: ")
        endereco = input("Digite o endereço: ")
        cpf = input("Digite o CPF: ")
        novo_usuario = PessoaFisica(endereco, nome, datetime.now(), cpf)
        self.usuarios.append(novo_usuario)
        print(f"\n=== Usuário Pessoa Física criado com sucesso: {nome} ===")

    def criar_usuario_juridica(self):
        nome = input("Digite a razão social: ")
        endereco = input("Digite o endereço: ")
        cnpj = input("Digite o CNPJ: ")
        novo_usuario = PessoaJuridica(endereco, nome, datetime.now(), cnpj)
        self.usuarios.append(novo_usuario)
        print(f"\n=== Usuário Pessoa Jurídica criado com sucesso: {nome} ===")

    def listar_contas(self):
        print("\n=== Lista de Contas ===")
        for conta in self.contas:
            print(f"{conta}")

    def processar_conta(self, escolha):
        numero_conta = input("Digite o número da conta: ")
        conta = self.encontrar_conta(numero_conta)
        if not conta:
            print("Conta não encontrada!")
            return

        if escolha == 'd':
            valor_deposito = float(input("Digite o valor do depósito: "))
            transacao = Deposito(valor_deposito)
            self.realizar_transacao(conta, transacao)
        elif escolha == 's':
            valor_saque = float(input("Digite o valor do saque: "))
            transacao = Saque(valor_saque)
            self.realizar_transacao(conta, transacao)
        elif escolha == 'e':
            self.exibir_extrato(conta)

    def encontrar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta
        return None

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        print("Transação realizada com sucesso!")

    def exibir_extrato(self, conta):
        print(f"\n=== Extrato da Conta ===")
        print(f"Titular: {conta.cliente.nome}")
        print(f"Número da Conta: {conta.numero}")
        print(f"Saldo: R$ {conta.saldo}")
        print(f"Histórico de Transações:")
        for transacao in conta.historico.transacoes:
            print(f"Data: {transacao['data']}, Tipo: {transacao['tipo']}, Valor: {transacao['valor']}")
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nasc, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"
class PessoaJuridica(Cliente):
    def __init__(self, endereco, razao_social, data_criacao, cnpj):
        super().__init__(endereco)
        self.razao_social = razao_social
        self.data_criacao = data_criacao
        self.cnpj = cnpj

    def __str__(self):
        return f"Razão Social: {self.razao_social}, CNPJ: {self.cnpj}"
class Conta(ABC):
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        if valor > self._saldo + self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False
        elif len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]) >= self.limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def __str__(self):
        return f"Conta Corrente - Número: {self.numero}, Saldo: R$ {self.saldo}"
class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor):
        if valor > self._saldo:
            print("\n@@@ Operação falhou! Você não possui saldo suficiente. @@@")
            return False
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    def __str__(self):
        return f"Conta Poupança - Número: {self.numero}, Saldo: R$ {self.saldo}"
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


if __name__ == "__main__":
    app = Main()
    app.executar()
