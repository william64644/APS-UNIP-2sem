"""
Essse script realiza testes nas funções do módulo SES
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


def test_adicionarZerosNecessarios():
    entrada = "011000010110001001100011"
    saidaEsperada = "00000000011000010110001001100011"
    saida = s.adicionarZerosNecessarios(entrada)
    if saida == None:
        return saida
    if saida == saidaEsperada:
        return False
    else:
        return True


def test_removerZerosNecessarios():
    entrada = "00000000011000010110001001100011"
    saidaEsperada = "011000010110001001100011"
    saida = s.removerZerosNecessarios(entrada)
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


# Lista de todos as funções de teste
testes = [
    test_dnl0, test_dnl1, test_dnl0reverso, test_dnl1reverso,
    test_textoParaStringBinaria, test_stringBinariaParaTexto,
    test_adicionarZerosNecessarios, test_removerZerosNecessarios,
    test_stringBinariaParaBlocos
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
