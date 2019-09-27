import pytest 
from com.moreaux.convert_hora import converteHora

def test_conver_hora():
    assert converteHora(17, 10) == '05:10 PM'

def test_conver_hora2():
    assert converteHora(23, 23) == '11:23 PM'

def test_conver_hora3():
    assert converteHora(24, 60) == None

def test_conver_hora4():
    assert converteHora(13, 10) == '01:10 PM'

def test_hora4():
    assert converteHora(0, 0) == '12:00 AM'