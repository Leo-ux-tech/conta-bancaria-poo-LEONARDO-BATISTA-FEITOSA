class ContaBancaria:
    def _init_(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def exibir_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo R${self.saldo:.2f}")

# Teste simples
conta = ContaBancaria("Leonardo Batista", 10000)
conta.exibir_saldo()
