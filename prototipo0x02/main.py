"""

    DESCONTINUADO

"""

"""
CARACTERÍSTICAS DO ALGORÍTIMO
Cifra de blocos de 16 bytes
bytes são embaralhados de acordo com a chave para aumentar a entropia
00 - dividir o bloco em 1 par e alternar a posição dos pares
01 - dividir o bloco em 2 pares e alternar a posição dos pares
10 - dividir o bloco em 4 pares e alternar a posição dos pares
11 - dividir o bloco em 8 pares e alternar a posição dos pares

para cada 2 bits usados para alternar os bytes, performar um XOR entre cada byte do bloco e a chave
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

def strByteArr(string):
    return (' '.join('{0:08b}'.format(ord(x), 'b') for x in string)).split()
    
def byteArrStr(binArr):
    out = ""
    for bin in binArr:
        out += chr(binaryInt(bin))
    return out

def strBinArr(string):
    return (' '.join('{0:08b}'.format(ord(x), 'b') for x in string)).split()
    
def calcularChave(stringKey):
    binary = strBinArr(stringKey)
    out = binary[0]
    for i in range(len(binary)-1):
        out = XOR(out, binary[i+1])

    return out

# 00 - dividir o bloco em 1 par de 8 bytes e alternar a posição dos pares
def alternar00(byteArr):
    if (len(byteArr) != 16):
        raise Exception("Esse algorítimo opera exclusivamente com blocos de 16 bytes!")
    else:
        buffer = byteArr[0:8]
        byteArr[0:8] = byteArr[8:16]
        byteArr[8:16] = buffer
        return byteArr

# 01 - dividir o bloco em 2 pares de 4 bytes e alternar a posição dos pares
def alternar01(byteArr):
    if (len(byteArr) != 16):
        raise Exception("Esse algorítimo opera exclusivamente com blocos de 16 bytes!")
    else:
        buffer = byteArr[0:4]
        byteArr[0:4] = byteArr[4:8]
        byteArr[4:8] = buffer

        buffer = byteArr[8:12]
        byteArr[8:12] = byteArr[12:16]
        byteArr[12:16] = buffer
        return byteArr

# 10 - dividir o bloco em 4 pares de 2 bytes e alternar a posição dos pares
def alternar10(byteArr):
    if (len(byteArr) != 16):
        raise Exception("Esse algorítmo opera exclusivamente com blocos de 16 bytes!")
    else:
        buffer = byteArr[0:2]
        byteArr[0:2] = byteArr[2:4]
        byteArr[2:4] = buffer

        buffer = byteArr[4:6]
        byteArr[4:6] = byteArr[6:8]
        byteArr[6:8] = buffer

        buffer = byteArr[8:10]
        byteArr[8:10] = byteArr[10:12]
        byteArr[10:12] = buffer

        buffer = byteArr[12:14]
        byteArr[12:14] = byteArr[14:16]
        byteArr[14:16] = buffer
        
        return byteArr

# 11 - dividir o bloco em 8 pares de 1 byte alternar a posição dos pares
def alternar11(byteArr):
    if (len(byteArr) != 16):
        raise Exception("Esse algorítmo opera exclusivamente com blocos de 16 bytes!")
    else:
        for i in range(0, len(byteArr)-1, 2):
            buffer = byteArr[i]
            byteArr[i] = byteArr[i+1]
            byteArr[i+1] = buffer
        return byteArr

    

def criptografar(entrada, chave):
    entradaBin = strBinArr(entrada)
    chave = calcularChave(chave)
    criptografado = []
    for byte in entradaBin:
        criptografado.append(chr(binaryInt(XOR(byte, chave))))
        
    for i in range(7):
        if (chave[i:i+2] == "00"):
            criptografado = alternar00(criptografado)
        elif (chave[i:i+2] == "01"):
            criptografado = alternar01(criptografado)
        elif (chave[i:i+2] == "10"):
            criptografado = alternar10(criptografado)
        elif (chave[i:i+2] == "11"):
            criptografado = alternar11(criptografado)
    return criptografado

descriptografar = criptografar

data = "0123456789abcdef"
chave = "vgbh"
print(data)
out = criptografar(data, chave)
print(''.join(out))

out = criptografar(out, chave)
print(''.join(out))