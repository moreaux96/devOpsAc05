import pytest
from com.moreaux.conta_corrente import ContaCorrente

conta_corrente = ContaCorrente(1, "Anna Flávia", 0.0)

def test_alterarNome():
    conta_corrente.alterarNome("Anna Flávia")
    assert conta_corrente.nomeCorrentista == "Anna Flávia"

def test_deposito():
    conta_corrente.deposito(500)
    assert conta_corrente.saldo == 500
    conta_corrente.deposito(50)
    assert conta_corrente.saldo == 200
    
def test_saque():
    conta_corrente.saque(199)
    assert conta_corrente.saldo == 1