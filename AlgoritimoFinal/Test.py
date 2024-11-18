"""
Essse script realiza testes nas funções do módulo SES
"""

from SES import SES

s = SES()

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
    if saida == None:
        return saida
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
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_dnl0reverso():
    entrada = [['00', '00', '00', '01'],
               ['11', '01', '00', '11'],
               ['11', '00', '10', '00'],
               ['00', '11', '11', '00']]
    saidaEsperada = [['00', '11', '00', '01'],
                     ['00', '11', '00', '10'],
                     ['00', '11', '00', '11'],
                     ['00', '11', '01', '00']]
    saida = s.dnl0reverso(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_dnl1reverso():
    entrada = [['00', '11', '00', '11'],
               ['10', '01', '01', '00'],
               ['01', '10', '11', '01'],
               ['10', '01', '10', '10']]
    saidaEsperada = [['11', '10', '01', '11'],
                     ['11', '01', '00', '00'],
                     ['10', '10', '01', '01'],
                     ['00', '10', '01', '10']]
    saida = s.dnl1reverso(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_textoParaStringBinaria():
    entrada = "abcd"
    saidaEsperada = "01100001011000100110001101100100"
    saida = s.textoParaStringBinaria(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_stringHEXparaStringBinaria():
    entrada = "42DA9EED"
    saidaEsperada = "01000010110110101001111011101101"
    saida = s.stringHEXparaStringBinaria(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True

def test_stringBinariaParaTexto():
    entrada = "01100001011000100110001101100100"
    saidaEsperada = "abcd"
    saida = s.stringBinariaParaTexto(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True

def test_stringBinariaParaBlocos():
    entrada = "0110000101100010011000110110010001100101011001100110011101101000"
    saidaEsperada = ["01100001011000100110001101100100",
                     "01100101011001100110011101101000"]
    saida = s.stringBinariaParaBlocos(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_blocoParaMatriz():
    entrada = "01100011011001000011000100110010"
    saidaEsperada = [['01', '10', '00', '11'],
                     ['01', '10', '01', '00'],
                     ['00', '11', '00', '01'],
                     ['00', '11', '00', '10']]
    saida = s.blocoParaMatriz(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_matrizParaBloco():
    entrada = [['01', '10', '00', '11'],
               ['01', '10', '01', '00'],
               ['00', '11', '00', '01'],
               ['00', '11', '00', '10']]
    saidaEsperada = "01100011011001000011000100110010"
    saida = s.matrizParaBloco(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_matrizParaStringHEX():
    entrada = [['01', '00', '00', '10'],
               ['11', '01', '10', '10'],
               ['10', '01', '11', '10'],
               ['11', '10', '11', '01']]
    saidaEsperada = "42DA9EED"
    saida = s.matrizParaStringHEX(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_calcularXORMatrizes():
    matriz1 = [['10', '00', '01', '00'],
               ['11', '00', '01', '00'],
               ['11', '00', '10', '00'],
               ['01', '01', '11', '10']]
    matriz2 = [['11', '00', '01', '10'],
               ['00', '01', '11', '10'],
               ['01', '01', '01', '10'],
               ['10', '11', '00', '11']]
    saidaEsperada = [['01', '00', '00', '10'],
                     ['11', '01', '10', '10'],
                     ['10', '01', '11', '10'],
                     ['11', '10', '11', '01']]
    saida = s.calcularXORMatrizes(matriz1, matriz2)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_stringHEXparaMatriz():
    entrada = "42DA9EED"
    saidaEsperada = [['01', '00', '00', '10'],
                     ['11', '01', '10', '10'],
                     ['10', '01', '11', '10'],
                     ['11', '10', '11', '01']]
    saida = s.stringHEXparaMatriz(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True

# Lista de todos as funções de teste
testes = [
    test_dnl0, test_dnl1, test_dnl0reverso, test_dnl1reverso,
    test_textoParaStringBinaria, test_stringBinariaParaTexto,
    test_stringBinariaParaBlocos, test_blocoParaMatriz, test_matrizParaBloco,
    test_matrizParaStringHEX, test_calcularXORMatrizes,
    test_stringHEXparaMatriz, test_stringHEXparaStringBinaria
]

for teste in testes:
    resultado = teste()
    nomeFuncao = teste.__name__[5:]
    if resultado == False:
        print(f"✅ Teste {nomeFuncao} bem-sucedido")
    elif resultado == True:
        print(f"❌ Teste {nomeFuncao} mal-sucedido")
    else:
        print(
            f"⬜ Função {nomeFuncao} ainda não implementada")


