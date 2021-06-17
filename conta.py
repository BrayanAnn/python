class Conta:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

conta1 = Conta('123-4', 'José', 1000)
print(conta1.saldo)
print(dir(conta1))

