import pytest
from com.moreaux.calculo_parcela import valorPagamento

def test_calculoPagamento1():
	assert valorPagamento(-10, 50) == None


def test_calculoPagamento2():
	assert valorPagamento(80, 10) == 90.4


def test_calculoPagamento3():
	assert valorPagamento(70, 0) == 70