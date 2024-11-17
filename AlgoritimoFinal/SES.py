"""
Essse é o módulo onde são definidas as funções necessárias para o processo de criptografia e descriptografia.

Definição dos termos usados no código desse projeto:
mensagem: O texto que o usuário digita para ser criptografado
chave: A chave em forma de texto digitada em forma de texto
bloco: Uma string de 32 bits. Exemplo: "01100001011000100110001101100100"
string binária: Uma string composta por N bits, não necessáriamente 32
matriz: Uma lista contendo 4 listas, cada uma contendo 4 pares de 2 bits. Exemplo: [['01','10','00','11'],['01','10','01','00'],['00','11','00','01'],['00','11','00','10']]


O processo de criptografia foi implementado de forma gráfica em uma planilha do Googe Sheets disponível em:
https://docs.google.com/spreadsheets/d/1Q1zWAQPs8pOOpE01QaQFARhuPik_b__1QvNb1AEtX6g/edit?usp=sharing
"""

from copy import deepcopy

class SES:

    MATRIZ_VAZIA = [['00', '00', '00', '00'],
                    ['00', '00', '00', '00'],
                    ['00', '00', '00', '00'],
                    ['00', '00', '00', '00']]

    substituicoes = {
        '00':'10',
        '10':'00',
        '01':'11',
        '11':'01'
    }

    substituicoesReverso = {
        '10': '00',
        '00': '10',
        '11': '01',
        '01': '11'
    }

    # Recebe uma matriz e retorna o seu respectivo deslocamento não linear 0
    def dnl0(self, matriz):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        buffer = matriz[0][0]
        matriz[0][0] = matriz[1][2]
        matriz[1][2] = matriz[3][3]
        matriz[3][3] = matriz[0][2]
        matriz[0][2] = matriz[3][0]
        matriz[3][0] = matriz[2][2]
        matriz[2][2] = matriz[1][3]
        matriz[1][3] = matriz[1][1]
        matriz[1][1] = matriz[0][3]
        matriz[0][3] = matriz[3][2]
        matriz[3][2] = matriz[2][1]
        matriz[2][1] = matriz[1][0]
        matriz[1][0] = matriz[0][1]
        matriz[0][1] = matriz[2][0]
        matriz[2][0] = matriz[3][1]
        matriz[3][1] = matriz[2][3]
        matriz[2][3] = buffer
        return matriz

    # Recebe uma matriz e retorna o seu respectivo deslocamento não linear 1
    def dnl1(self, matriz):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        buffer = matriz[0][0]
        matriz[0][0] = matriz[1][3]
        matriz[1][3] = matriz[1][2]
        matriz[1][2] = matriz[1][1]
        matriz[1][1] = matriz[2][2]
        matriz[2][2] = matriz[0][3]
        matriz[0][3] = matriz[1][0]
        matriz[1][0] = matriz[3][1]
        matriz[3][1] = matriz[2][3]
        matriz[2][3] = matriz[0][2]
        matriz[0][2] = matriz[3][0]
        matriz[3][0] = matriz[2][0]
        matriz[2][0] = matriz[3][2]
        matriz[3][2] = matriz[2][1]
        matriz[2][1] = matriz[3][3]
        matriz[3][3] = matriz[0][1]
        matriz[0][1] = buffer
        return matriz

    # Recebe uma matriz e retorna o seu respectivo deslocamento não linear 0 invertido
    def dnl0reverso(self, matriz):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        buffer = matriz[2][3]
        matriz[2][3] = matriz[3][1]
        matriz[3][1] = matriz[2][0]
        matriz[2][0] = matriz[0][1]
        matriz[0][1] = matriz[1][0]
        matriz[1][0] = matriz[2][1]
        matriz[2][1] = matriz[3][2]
        matriz[3][2] = matriz[0][3]
        matriz[0][3] = matriz[1][1]
        matriz[1][1] = matriz[1][3]
        matriz[1][3] = matriz[2][2]
        matriz[2][2] = matriz[3][0]
        matriz[3][0] = matriz[0][2]
        matriz[0][2] = matriz[3][3]
        matriz[3][3] = matriz[1][2]
        matriz[1][2] = matriz[0][0]
        matriz[0][0] = buffer

        return matriz

    # Recebe uma matriz e retorna o seu respectivo deslocamento não linear 1 invertido
    def dnl1reverso(self, matriz):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        buffer = matriz[0][1]
        matriz[0][1] = matriz[3][3]
        matriz[3][3] = matriz[2][1]
        matriz[2][1] = matriz[3][2]
        matriz[3][2] = matriz[2][0]
        matriz[2][0] = matriz[3][0]
        matriz[3][0] = matriz[0][2]
        matriz[0][2] = matriz[2][3]
        matriz[2][3] = matriz[3][1]
        matriz[3][1] = matriz[1][0]
        matriz[1][0] = matriz[0][3]
        matriz[0][3] = matriz[2][2]
        matriz[2][2] = matriz[1][1]
        matriz[1][1] = matriz[1][2]
        matriz[1][2] = matriz[1][3]
        matriz[1][3] = matriz[0][0]
        matriz[0][0] = buffer
        return matriz

    def dnln(self, matriz, bits):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        for bit in bits:
            if bit == '0':
                matriz = self.dnl0(matriz)
            elif bit == '1':
                matriz = self.dnl1(matriz)
            else:
                print("Erro: Situação não esperada em DNLN")
        return matriz

    def dnlnReverso(self, matriz, bits):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        for bit in reversed(bits):
            if bit == '0':
                matriz = self.dnl0reverso(matriz)
            elif bit == '1':
                matriz = self.dnl1reverso(matriz)
            else:
                print("Erro: Situação não esperada em DNLN Reverso")
        return matriz

    def textoParaStringBinaria(self, texto):
        # Converte cada caractere para seu valor binário de 8 bits
        binario_completo = ''
        for caractere in texto:
            binario_8bits = format(ord(caractere), '08b')
            binario_completo += binario_8bits
        return binario_completo

    def stringBinariaParaTexto(self, stringBinaria):
        # Divide a string binária em blocos de 8 bits e converte cada bloco para caractere ASCII
        caracteres = []
        for i in range(0, len(stringBinaria), 8):
            bloco8bits = stringBinaria[i:i+8]
            caractere = chr(int(bloco8bits, 2))
            caracteres.append(caractere)
        return ''.join(caracteres)

    def stringHEXparaStringBinaria(self, stringHEX):
        # Converte cada caractere hexadecimal para seu valor binário de 4 bits
        binario_completo = ''
        for caractere_hex in stringHEX:
            binario_4bits = format(int(caractere_hex, 16), '04b')
            binario_completo += binario_4bits
        return binario_completo

    def adicionarNull(self, string):
        padding = (4 - len(string) % 4) % 4
        return string + '\0' * padding

    def removerNull(self, string):
        return string.replace('\0', '')

    def stringBinariaParaBlocos(self, stringBinaria):
        # Divide a string em blocos de 32 bits
        blocos_32bits = []
        for i in range(0, len(stringBinaria), 32):
            bloco = stringBinaria[i:i+32]
            blocos_32bits.append(bloco)
        return blocos_32bits

    def stringHexParaBlocosHex(self, stringhex):
        # Divide a string em blocos de 8 Hexadecimais
        blocos_8 = []
        for i in range(0, len(stringhex), 8):
            bloco = stringhex[i:i+8]
            blocos_8.append(bloco)
        return blocos_8

    def blocoParaMatriz(self, bloco):
        # Divide o bloco de 32 bits em uma matriz 4x4 com elementos de 2 bits
        matriz = []
        for i in range(0, 32, 8):
            linha = [bloco[i+j:i+j+2] for j in range(0, 8, 2)]
            matriz.append(linha)
        return matriz

    def matrizParaBloco(self, matriz):
        # Converte a matriz 4x4 de elementos de 2 bits em uma string binária de 32 bits
        binario_completo = ''
        for linha in matriz:
            binario_completo += ''.join(linha)
        return binario_completo

    def matrizParaStringHEX(self, matriz):
        # Converte cada linha da matriz de 4 elementos de 2 bits em um valor hexadecimal com 2 dígitos
        stringHEX = ''
        for linha in matriz:
            bits_linha = ''.join(linha)
            valor_hex = format(int(bits_linha, 2), '02X')  # Garante 2 dígitos com zero à esquerda
            stringHEX += valor_hex
        return stringHEX


    def xor2Bits(self, bitString1, bitString2):
        resultado_xor = ''
        for k in range(2):
            bit_xor = str(int(bitString1[k]) ^ int(bitString2[k]))
            resultado_xor += bit_xor
        return resultado_xor

    def calcularXORMatrizes(self, matriz1, matriz2):
        # Realiza operação XOR elemento a elemento entre duas matrizes 4x4 de elementos de 2 bits
        matriz_resultante = []
        for i in range(4):
            linha_xor = []
            for j in range(4):
                xor_bits = self.xor2Bits(matriz1[i][j], matriz2[i][j])
                linha_xor.append(xor_bits)
            matriz_resultante.append(linha_xor)
        return matriz_resultante

    def substituirMatriz(self, matriz):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        novaMatriz = self.MATRIZ_VAZIA
        for i, linha in enumerate(matriz):
            for j, bits in enumerate(linha):
                novaMatriz[i][j] = self.substituicoes[bits]
        return novaMatriz

    def substituirMatrizReverso(self, matriz):
        matriz = deepcopy(matriz)  # Não alterar a matriz de origem
        novaMatriz = self.MATRIZ_VAZIA
        for i, linha in enumerate(matriz):
            for j, bits in enumerate(linha):
                novaMatriz[i][j] = self.substituicoesReverso[bits]
        return novaMatriz

    def stringHEXparaMatriz(self, stringHEX):
        stringBinaria = self.stringHEXparaStringBinaria(stringHEX)
        matriz = []
        for i in range(0, 32, 8):
            linha = [stringBinaria[i+j:i+j+2] for j in range(0, 8, 2)]
            matriz.append(linha)
        return matriz

    def comprimirMatrizes(self, matrizes):
        matriz_resultante = matrizes[0]
        for matriz in matrizes[1:]:
            matriz_resultante = self.calcularXORMatrizes(
                matriz_resultante, matriz)
        return matriz_resultante

    def stringParaMatrizes(self, string):
        stringBinaria = self.textoParaStringBinaria(string)
        blocos = self.stringBinariaParaBlocos(stringBinaria)

        matrizes = []
        for bloco in blocos:
            matriz = self.blocoParaMatriz(bloco)
            matrizes.append(matriz)
        return matrizes

    def gerarBitsDnln(self, matriz):
        bits_dnln = []
        for linha in matriz:
            bits_resultantes = linha[0]
            for elemento in linha[1:]:
                bits_resultantes = self.xor2Bits(bits_resultantes, elemento)
            bits_dnln.append(bits_resultantes)
        return ''.join(bits_dnln)

    def expandirChave0(self, chave0):
        chaves = []
        chaves.append(self.dnl0(chave0))
        for i in range(3):
            chaves.append(self.dnl0(chaves[i]))
        resultadoDnl0 = deepcopy(chaves)
        for i, matriz in enumerate(chaves):
            chaves[i] = self.calcularXORMatrizes(chaves[i], chave0)
            chaves[i] = self.dnl1(chaves[i])
            chaves[i] = self.calcularXORMatrizes(chaves[i], resultadoDnl0[i])
        return chaves

    def criptografarMatriz(self, matrizMensagem, chaves, chave0):
        estado = matrizMensagem
        estado = self.substituirMatriz(estado)
        estado = self.dnl0(estado)
        estado = self.calcularXORMatrizes(estado, chaves[0])
        estado = self.substituirMatriz(estado)
        estado = self.dnl1(estado)
        estado = self.calcularXORMatrizes(estado, chaves[1])
        estado = self.substituirMatriz(estado)
        estado = self.dnl0(estado)
        estado = self.calcularXORMatrizes(estado, chaves[2])
        estado = self.substituirMatriz(estado)
        estado = self.dnl1(estado)
        estado = self.calcularXORMatrizes(estado, chaves[3])
        bitsDnln = self.gerarBitsDnln(chave0)
        estado = self.dnln(estado, bitsDnln)
        return estado

    def descriptografarMatriz(self, matrizCriptografada, chaves, chave0):
        estado = deepcopy(matrizCriptografada)
        bitsDnln = self.gerarBitsDnln(chave0)
        estado = self.dnlnReverso(estado, bitsDnln)
        estado = self.calcularXORMatrizes(estado, chaves[3])
        estado = self.dnl1reverso(estado)
        estado = self.substituirMatrizReverso(estado)
        estado = self.calcularXORMatrizes(estado, chaves[2])
        estado = self.dnl0reverso(estado)
        estado = self.substituirMatrizReverso(estado)
        estado = self.calcularXORMatrizes(estado, chaves[1])
        estado = self.dnl1reverso(estado)
        estado = self.substituirMatrizReverso(estado)
        estado = self.calcularXORMatrizes(estado, chaves[0])
        estado = self.dnl0reverso(estado)
        estado = self.substituirMatrizReverso(estado)
        return estado

    def criptografar(self, mensagem, chave):
        if (chave == ""):
            return mensagem
        mensagem = self.adicionarNull(mensagem)
        chave = self.adicionarNull(chave)
        mensagemMatrizes = self.stringParaMatrizes(mensagem)
        chave0 = self.comprimirMatrizes(self.stringParaMatrizes(chave))
        chaves = self.expandirChave0(chave0)

        criptografadoMatrizes = []
        for mensagemMatriz in mensagemMatrizes:
            criptografadoMatrizes.append(
                self.criptografarMatriz(mensagemMatriz, chaves, chave0))

        mensagemCriptografada = ""
        for criptografadoMatriz in criptografadoMatrizes:
            mensagemCriptografada += self.matrizParaStringHEX(
                criptografadoMatriz)

        return mensagemCriptografada

    def descriptografar(self, hexCriptografado, chave):
        if (chave == ""):
            return hexCriptografado
        chave = self.adicionarNull(chave)
        chave0 = self.comprimirMatrizes(self.stringParaMatrizes(chave))
        chaves = self.expandirChave0(chave0)
        blocosCriptografados = self.stringHexParaBlocosHex(hexCriptografado)
        blocosBinarios = []
        for blocoCriptografado in blocosCriptografados:
            matrizCriptografada = self.stringHEXparaMatriz(blocoCriptografado)
            matrizDescriptografada = self.descriptografarMatriz(
                matrizCriptografada, chaves, chave0)
            blocosBinarios.append(self.matrizParaBloco(matrizDescriptografada))

        mensagem = ""
        for bloco in blocosBinarios:
            mensagem += self.stringBinariaParaTexto(bloco)
            
        mensagem = self.removerNull(mensagem)
        return mensagem

    def exibirMatriz(self, matriz):
        # (Apenas para debug)
        print('+-----------+')
        for linha in matriz:
            print('|', end='')
            for byte in linha:
                print(byte, end='')
                print('|', end='')
            print('')
        print('+-----------+')

    def exibirMatrizes(self, matrizes):
        # (Apenas para debug)
        for i, matriz in enumerate(matrizes, start=1):
            print(f"Matriz {i}:")
            self.exibirMatriz(matriz)
            print('')
