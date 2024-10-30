"""
Esse script é utilizado para validar cada função e operação do módulo SES
"""

from SES import SES as s

def test_dnl0():
    entrada = [['00', '11', '00', '01'],
['00', '11', '00', '10'],
['00', '11', '00', '11'],
['00', '11', '01', '00']]
    
    saidaEsperada = [['00', '00', '00', '01'],
['11', '01', '00', '11'],
['11', '00', '10', '00'],
['00', '11', '11', '00']]
    
    saida = s.dnl0(entrada)

    if saida == saidaEsperada:
        return False
    else:
        return True

def test_dnl1():
    entrada = [['11', '10', '01', '11'],
['11', '01', '00', '00'],
['10', '10', '01', '01'],
['00', '10', '01', '10']]
    

    
    saidaEsperada = [['00', '11', '00', '11'],
['10', '01', '01', '00'],
['01', '10', '11', '01'],
['10', '01', '10', '10']]
    
    saida = s.dnl1(entrada)

    if saida == saidaEsperada:
        return False
    else:
        return True

print(test_dnl0())
print(test_dnl1())