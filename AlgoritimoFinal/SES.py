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
class SES:
    
    mensagem = ''
    mensagemBinario = ''
    
    chave = ''
    chaveBinario = ''

    criptografadoHEX = ''

    # Matriz que armazena o estado atual durante o processo de criptografia/descriptografia
    estado = []
    
    chaveMatriz = []

    
    substituicoes = {
        '00':'10',
        '10':'00',
        '01':'11',
        '11':'01'
    }

    # Recebe uma matriz e retorna o seu respectivo deslocamento não linear 0
    def dnl0(self, matriz):
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
        buffer = matriz[0][0]
        matriz[0][0] = matriz[1][3]
        matriz[1][3] = matriz[1][2]
        matriz[1][2] = matriz[1][1]
        matriz[1][2] = matriz[2][2]
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
            bloco_8bits = stringBinaria[i:i+8]
            caractere = chr(int(bloco_8bits, 2))
            caracteres.append(caractere)
        return ''.join(caracteres)

    def stringHEXparaStringBinaria(self, stringHEX):
        # Converte cada caractere hexadecimal para seu valor binário de 4 bits
        binario_completo = ''
        for caractere_hex in stringHEX:
            binario_4bits = format(int(caractere_hex, 16), '04b')
            binario_completo += binario_4bits
        return binario_completo

    def adicionarZerosNecessarios(self, stringBinaria):
        # Calcula quantos zeros são necessários para o comprimento ser múltiplo de 32
        comprimento_atual = len(stringBinaria)
        complemento = (32 - comprimento_atual % 32) % 32
        zeros_necessarios = '0' * complemento
        return zeros_necessarios + stringBinaria

    def removerZerosNecessarios(self, stringBinaria):
        # Remove blocos de 8 bits iguais a '00000000' no início da string
        while stringBinaria.startswith('00000000'):
            stringBinaria = stringBinaria[8:]
        return stringBinaria

    def stringBinariaParaBlocos(self, stringBinaria):
        # Divide a string em blocos de 32 bits
        blocos_32bits = []
        for i in range(0, len(stringBinaria), 32):
            bloco = stringBinaria[i:i+32]
            blocos_32bits.append(bloco)
        return blocos_32bits

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
        # Converte cada linha da matriz de 4 elementos de 2 bits em um valor hexadecimal
        stringHEX = ''
        for linha in matriz:
            bits_linha = ''.join(linha)
            valor_hex = format(int(bits_linha, 2), 'X')
            stringHEX += valor_hex
        return stringHEX

    def calcularXORMatrizes(self, matriz1, matriz2):
        # Realiza operação XOR elemento a elemento entre duas matrizes 4x4 de elementos de 2 bits
        matriz_resultante = []
        for i in range(4):
            linha_xor = []
            for j in range(4):
                xor_bits = format(int(matriz1[i][j], 2) ^ int(
                    matriz2[i][j], 2), '02b')
                linha_xor.append(xor_bits)
            matriz_resultante.append(linha_xor)
        return matriz_resultante

    def stringHEXparaMatriz(self, stringHEX):
        # Usa stringHEXparaStringBinaria para converter a string hexadecimal para binário
        stringBinaria = self.stringHEXparaStringBinaria(stringHEX)
        # Divide a string binária em uma matriz 4x4 de elementos de 2 bits
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
        stringBinaria = self.adicionarZerosNecessarios(stringBinaria)
        blocos = self.stringBinariaParaBlocos(stringBinaria)

        matrizes = []
        for bloco in blocos:
            matriz = self.blocoParaMatriz(bloco)
            matrizes.append(matriz)
        return matrizes

    def xor2Bits(self, bitString1, bitString2):
        resultado_xor = ''
        for k in range(2):
            bit_xor = str(int(bitString1[k]) ^ int(bitString2[k]))
            resultado_xor += bit_xor
        return resultado_xor

    def gerarBitsDnln(self, matriz):
        bits_dnln = []
        for linha in matriz:
            bits_resultantes = linha[0]
            for elemento in linha[1:]:
                bits_resultantes = self.xor2Bits(bits_resultantes, elemento)
            bits_dnln.append(bits_resultantes)
        return ''.join(bits_dnln)

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
