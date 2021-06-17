class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Conta número: {}, Saldo: {}" .format(self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Retirada de {} feito com sucesso".format(valor))
            return True
        else:
            print("Não foi possível realizar o saque\nSaldo inferior ao valor do saque")
            return False

    def deposita(self, valor):
        self.saldo += valor
        print("Depositou: {}, novo saldo: {}". format(valor, self.saldo))

    def tranferencia(self, destino, valor):
        if (self.saque(valor)):
            self.saque(valor)
            destino.deposita(valor)
            print("Transferência para {} concluída com sucesso" .format(destino.numero))
        else:
            print("Não foi possível fazer a trasferencia")

    def infos(self):
        print("Nome: {}\nSObrenome: {}\nCPF: {}".format(self.titular.nome, self.titular.sobrenome, self.titular.cpf))


cliente = Cliente('João', 'Silva', '845568798')
cliente1 = Cliente('Pedro', 'Silva', '8728398892')
conta = Conta('1234-4', cliente, 1400.00, 2600.00)
conta1 = Conta('1234-5', cliente1, 1200.00, 3000.00)
conta.tranferencia(conta1, 200)
conta.extrato()
conta.infos()
conta1.extrato()
conta1.infos()
