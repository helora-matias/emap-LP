class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def __str__(self):
        print(f"Titular: {self.titular}, Saldo: {self._saldo}")
    
    def __eq__(self, outro):
        return self.titular == outro.titular and self._saldo == outro._saldo

tit1 = ContaBancaria("Helora", 0.0)
tit1.__str__()

tit2 = ContaBancaria("Kelly", 10.0)
print(tit1 == tit2)

class Peca:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def __str__(self):
        print(f"Tipo da Peça: {self.tipo}, Cor da Peça: {self.cor}")
    
    def __eq__(self, outra):
        return self.tipo == outra.tipo
    
def combinar_peca(*args):
    comb = []
    for peca1 in args:
        
        i = 1
        if i < 4:
            peca2 = args[i]
            if peca1 == peca2:
                peca1.__str__()
                comb.append(peca1)
                comb.append(peca2)
    return comb

rei = Peca('Rei', 'Branca')
rainha = Peca('Rainha', 'Branca')
cavalop = Peca('Cavalo', 'Preta')
cavalob = Peca('Cavalo', 'Branco')

combinar_peca(rei, rainha, cavalob, cavalop)



