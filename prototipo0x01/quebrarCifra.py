"""

    DESCONTINUADO

"""

import os
from prettytable import PrettyTable

def limpar():
    os.system("cls || clear")

def xor(a, b):
    if (a != "0" and a != "1") or (b != "0" and b != "1"):
        print("WARNING: xor(a, b) is meant for binary only!")
    if a != b:
        return "1"
    else:
        return "0"

letrasFrequenciasReal = [['a', 0.1463], ['b', 0.0104], ['c', 0.0388], ['d', 0.0499], ['e', 0.1257], ['f', 0.0102], ['g', 0.013], ['h', 0.0128], ['i', 0.0618], ['j', 0.004], ['k', 0.0002], ['l', 0.0278], ['m', 0.0474], ['n', 0.0505], ['o', 0.1073], ['p', 0.0252], ['q', 0.012], ['r', 0.0653], ['s', 0.0781], ['t', 0.0434], ['u', 0.0463], ['v', 0.0167], ['w', 0.0001], ['x', 0.0021], ['y', 0.0001], ['z', 0.0047], [' ', 0.1422]]
# Ordenar lista pela frequência
letrasFrequenciasRealUnsorted = letrasFrequenciasReal
letrasFrequenciasReal.sort(key=lambda x: x[1], reverse=True)

hexValidos = ['61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '20']

mapaHexChar = {
    '20': ' ',
    '61': 'a',
    '62': 'b',
    '63': 'c',
    '64': 'd',
    '65': 'e',
    '66': 'f',
    '67': 'g',
    '68': 'h',
    '69': 'i',
    '6a': 'j',
    '6b': 'k',
    '6c': 'l',
    '6d': 'm',
    '6e': 'n',
    '6f': 'o',
    '70': 'p',
    '71': 'q',
    '72': 'r',
    '73': 's',
    '74': 't',
    '75': 'u',
    '76': 'v',
    '77': 'w',
    '78': 'x',
    '79': 'y',
    '7a': 'z'
}

mapaCharHex = {
    ' ': '20',
    'a': '61',
    'b': '62',
    'c': '63',
    'd': '64',
    'e': '65',
    'f': '66',
    'g': '67',
    'h': '68',
    'i': '69',
    'j': '6a',
    'k': '6b',
    'l': '6c',
    'm': '6d',
    'n': '6e',
    'o': '6f',
    'p': '70',
    'q': '71',
    'r': '72',
    's': '73',
    't': '74',
    'u': '75',
    'v': '76',
    'w': '77',
    'x': '78',
    'y': '79',
    'z': '7a'
}
def addChar(text,char,place):
  return text[:place] + char + text[place:]

def printBytes(byteString, tamanhoByte=8):
    contador = 0
    for bit in byteString:
        print(bit, end='')
        contador += 1
        if (contador == tamanhoByte):
            print(' ', end='')
            contador = 0
    print()

# "ABC" => "010000010100001001000011"
def strBinary(string):
    binary_string = ""
    for char in string:
        binary_string += bin(ord(char))[2:].zfill(8)
    return binary_string

# "ABC" => "414243"
def strHex(string):
    hex_string = ""
    for char in string:
        hex_string += hex(ord(char))[2:].zfill(2)
    return hex_string

# "011000010110001001100011" => ["61", "6a", "6a"]
def binaryToHexList(binaryString):
    # Split the binary string into chunks of 8 bits
    eight_bit_chunks = [binaryString[i:i+8] for i in range(0, len(binaryString), 8)]
    
    # Convert each 8-bit chunk to hexadecimal
    hex_values = []
    for bits in eight_bit_chunks:
        hex_value = hex(int(bits, 2))[2:]
        hex_values.append(hex_value)
    
    return hex_values

def addZerosEsquerda(string, tamanhoBloco=32):
    zerosFaltando = 32 - (len(string) % tamanhoBloco)
    string = '0' * zerosFaltando + string
    return string

def criptografar(mensagem, chave):
    ciphered = []
    i = 0
    for i in range(len(mensagem)):
        bitMensagem = mensagem[i]
        bitChave = chave[i%len(chave)]
        ciphered.append(xor(bitMensagem, bitChave))
    return (''.join(ciphered))

# "aabc" => [['a', 0.5], ['b', 0.25], ['c', 0.25], ['d', 0.0], ..., ['z', 0.0]]
def calcularLetrasFrequencias(string):
    letrasContador = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, ' ': 0}

    letrasFrequencias = [['61', 0.0], ['62', 0.0], ['63', 0.0], ['64', 0.0], ['65', 0.0], ['66', 0.0], ['67', 0.0], ['68', 0.0], ['69', 0.0], ['6a', 0.0], ['6b', 0.0], ['6c', 0.0], ['6d', 0.0], ['6e', 0.0], ['6f', 0.0], ['70', 0.0], ['71', 0.0], ['72', 0.0], ['73', 0.0], ['74', 0.0], ['75', 0.0], ['76', 0.0], ['77', 0.0], ['78', 0.0], ['79', 0.0], ['7a', 0.0], ['20', 0.0000]]

    for char in string:
        if char in letrasContador:
            letrasContador[char] += 1

    for i, parContador in enumerate(letrasContador.items()):
        letrasFrequencias[i][1] = round(parContador[1] / len(string), 4)

    letrasFrequencias.sort(key=lambda x: x[1], reverse=True)
        
    return letrasFrequencias

# ["61", "6a", "6a"] => [['6a', 0.6666], ['61', 0.3333]]
def calculate_hex_ratios(hex_list):
    # Calculate the total number of hex values
    total_count = len(hex_list)
    
    # Create a dictionary to count occurrences of each hex value
    hex_count = {}
    for hex_value in hex_list:
        hex_count[hex_value] = hex_count.get(hex_value, 0) + 1
    
    # Calculate the ratio for each hex value
    hex_ratios = {hex_value: round(count / total_count,4) for hex_value, count in hex_count.items()}
    
    # Convert the dictionary to a list of lists and sort it in reverse order based on the ratio
    sorted_ratios = sorted([[hex_value, ratio] for hex_value, ratio in hex_ratios.items()], key=lambda x: x[1], reverse=True)
    
    return sorted_ratios


def gerarSaidaTabela(listaHex, substituicoes):
    letras = []
    for i, hexChar in enumerate(listaHex):
        if substituicoes[hexChar] not in hexValidos:
            letras.append("(0x"+hexChar+')')
        else:
            letras.append(mapaHexChar[substituicoes[hexChar]])


    return ''.join(letras)

def calcularAlturaMensagem(listaHex, substituicoes: dict, largura):
    encontrados = 0
    naoEncontrados = 0
    for hexChar in listaHex:
        if substituicoes[hexChar] in hexValidos:
            encontrados += 1
        else:
            naoEncontrados += 1
    comprimento = encontrados + naoEncontrados*6
    altura = int(comprimento/maxLen)+1
    return altura
    


opcao = ''
print("****************************************")
print("*         DECIFRADOR DE VERNAM         *")
print("****************************************")
entrada = """era uma vez uma aurora que apareceu ao amanhecer aquecendo as almas alegres que aguardavam a chegada do excelente e ensolarado dia e as pessoas sairam apressadas para abracar as atividades correndo pelas extensas e estreitas avenidas amplas e agradavel as criancas entusiasmadas e animadas agitavam as asas da imaginacao atravessando o parque alegremente pulando e correndo a cada passo as enormes e elegantes arvores altas abrigavam aves que alcavam voo voando pelo ar leve e refrescante enquanto as sombras comecavam a aparecer ao lado das estradas ensolaradas as folhas caiam formando um colorido tapete sobre o solo umido o outono chegou trazendo consigo um ar de renovacao a noite chegou e o ceu se tornou um manto negro adornado por incontaveis estrelas a lua redonda e brilhante iluminava o caminho enquanto os vagalumes dancavam ao sabor da brisa"""
#entrada = "bom dia"
entrada = input("Entre com a mensagem para ser criptografada: ")
entradaBin = strBinary(entrada)


letrasFrequencias = calcularLetrasFrequencias(entrada)

#chave = input("Entre com a chave da criptografia: ")
chave = "1111"
chaveBin = strBinary(chave)
criptografado = criptografar(entradaBin, chaveBin)

criptografadoListaHex = binaryToHexList(criptografado)

# Inicialmente, o mapa substitui cada HEX por ele mesmo
global substituicoes
substituicoes = {}
for hexChar in criptografadoListaHex:
    substituicoes[hexChar] = hexChar

while opcao != '0': 
    limpar()
    print("+---------------------------------------------------------------------------------------------------------+")
    print("|                                 D E C I F R A D O R   D E   V E R N A M                                 |")
    

    table = PrettyTable(["Letra", "HEX Orig.", "Freq.", "Freq. Obs.", "HEX Obs.", "Mensagem Atual"])
    table.align = "l"
    maxLen = 50
    hexRatios = calculate_hex_ratios(criptografadoListaHex)
    for i in range(max(27, len(hexRatios), calcularAlturaMensagem(criptografadoListaHex, substituicoes, maxLen))):
        if i < 27:
            letra = letrasFrequenciasReal[i][0]
            hexStr = strHex(letra)
            freqOrig = letrasFrequenciasReal[i][1]
        else:
            letra = ''
            hexStr = ''
            freqOrig = ''
        mensagemAtual = gerarSaidaTabela(criptografadoListaHex, substituicoes)
        hexRatios = calculate_hex_ratios(criptografadoListaHex)
        if i < len(hexRatios):
            hexObs = "0x" + hexRatios[i][0]
            freqObs = hexRatios[i][1]
        else:
            hexObs = ''
            freqObs = ''
        
        mensagemAtual = mensagemAtual[i*maxLen:(i+1)*maxLen] # TODO: This line probably isn't working as intended
        mensagemAtual = mensagemAtual + (' ' * max(0, maxLen-len(mensagemAtual)))
        table.add_row([letra, hexStr, freqOrig, freqObs, hexObs, mensagemAtual])

    print(table)
    print("Escolha uma opção: ")
    print("1 - Substituição")
    print("2 - Reverter substituição")
    print("3 - Substituição estatística automática")
    print("4 - Substituir letra")
    print("0 - Sair")
    opcao = input("=> ")

    if opcao == "1":
        alvo = input("Qual HEX será substituído: 0x")
        sub = input(f"0x{alvo} deve ser substituído por qual letra: ")
        substituicoes[alvo] = mapaCharHex[sub]
    if opcao == "2":
        hexName = input("Reverter qual código HEX: ")
        substituicoes[hexName] = hexName
    if opcao == "3":
        for i in range(27):

            letra = letrasFrequenciasReal[i][0]
            hexStr = strHex(letra)
            freqOrig = letrasFrequenciasReal[i][1]
            

            hexRatios = calculate_hex_ratios(criptografadoListaHex)
            if i < len(hexRatios):
                hexObs = hexRatios[i][0]
                freqObs = hexRatios[i][1]
            else:
                hexObs = ''
                freqObs = ''
            

            substituicoes[hexObs] = hexStr
    if opcao == "4":
        letraAlvo = input("Qual letra será substituída: ")
        global hexAlvo
        hexAlvo = mapaCharHex.get(letraAlvo.lower(), None)

        if not hexAlvo:
            print(f"Letra {letraAlvo} não encontrada no mapa.")
        else:
            novaLetra = input(f"Substituir letra {letraAlvo} por qual letra: ")
            hexNovaLetra = mapaCharHex.get(novaLetra.lower(), None)

            if not hexNovaLetra:
                print(f"Letra {novaLetra} não encontrada no mapa.")
            else:
                # Fazer a primeira substituição no dicionário de substituições
                chaveParaSubstituir = None
                for chave, valor in substituicoes.items():
                    if valor == hexAlvo:
                        chaveParaSubstituir = chave
                        break
                
                if chaveParaSubstituir:
                    substituicoes[chaveParaSubstituir] = hexNovaLetra

                # Fazer a segunda substituição invertida (letra nova por letra antiga)
                chaveParaReverter = None
                for chave, valor in substituicoes.items():
                    if valor == hexNovaLetra and chave != chaveParaSubstituir:
                        chaveParaReverter = chave
                        break
                
                if chaveParaReverter:
                    substituicoes[chaveParaReverter] = hexAlvo