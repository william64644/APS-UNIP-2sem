"""

    DESCONTINUADO

"""

"""
Algorítimo baseado em um simples XOR entre a chave
e a informação de entrada dividida em blocos de 8 bits

Defeitos:
Se uma informação criptografada for novamente criptografada novamente com a mesma chave, o algorítimo retorna a informação original
Vulnerável a ataques por análise estatística
Vulnerável a ataques por "força bruta" (brute force)
"""
def xor(bit1, bit2):
    if (bit1 != bit2):
        return '1'
    else:
        return '0'

def XOR(byte1, byte2):
    return ''.join(xor(byte1[i], byte2[i])for i in range(len(byte1)))

def intBinary(integer):
    return bin(integer)[2:]

def binaryInt(bin):
    return int(bin, 2)

def strBinArr(string):
    return (' '.join('{0:08b}'.format(ord(x), 'b') for x in string)).split()
    
def binArrStr(binArr):
    out = ""
    for bin in binArr:
        out += chr(binaryInt(bin))
    return out
    
def calcularChave(stringKey):
    binary = strBinArr(stringKey)
    out = binary[0]
    for i in range(len(binary)-1):
        out = XOR(out, binary[i+1])

    return out

def criptografar(entrada, chave):
    entradaBin = strBinArr(entrada)
    chave = calcularChave(chave)
    criptografado = []
    for byte in entradaBin:
        criptografado.append(chr(binaryInt(XOR(byte, chave))))
    return criptografado

descriptografar = criptografar

data = "abc123"
key = "1"
criptografado = criptografar(data, key)
print(criptografado)
descriptografado = descriptografar(criptografado, key)
print(descriptografado)