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
        return ''.join(format(ord(c), '08b') for c in texto)

    def stringBinariaParaTexto(self, stringBinaria):
        # Divide a string binária em blocos de 8 bits e converte cada bloco para caractere ASCII
        caracteres = [stringBinaria[i:i+8]
                      for i in range(0, len(stringBinaria), 8)]
        return ''.join(chr(int(c, 2)) for c in caracteres)

    def stringHEXparaStringBinaria(self, stringHEX):
        # Converte cada caractere hexadecimal para seu valor binário de 4 bits
        return ''.join(format(int(c, 16), '04b') for c in stringHEX)

    def adicionarZerosNecessarios(self, stringBinaria):
        # Calcula quantos zeros são necessários para o comprimento ser múltiplo de 32
        complemento = (32 - len(stringBinaria) % 32) % 32
        return '0' * complemento + stringBinaria

    def removerZerosNecessarios(self, stringBinaria):
        # Remove blocos de 8 bits iguais a '00000000' no início da string
        while stringBinaria.startswith('00000000'):
            stringBinaria = stringBinaria[8:]
        return stringBinaria

    def stringBinariaParaBlocos(self, stringBinaria):
        # Divide a string em blocos de 32 bits
        return [stringBinaria[i:i+32] for i in range(0, len(stringBinaria), 32)]

    def blocoParaMatriz(self, bloco):
        # Divide o bloco de 32 bits em uma matriz 4x4 com elementos de 2 bits
        return [[bloco[i+j:i+j+2] for j in range(0, 8, 2)] for i in range(0, 32, 8)]

    def matrizParaBloco(self, matriz):
        # Converte a matriz 4x4 de elementos de 2 bits em uma string binária de 32 bits
        return ''.join(''.join(linha) for linha in matriz)

    def matrizParaStringHEX(self, matriz):
        # Converte cada linha da matriz de 4 elementos de 2 bits em um valor hexadecimal
        return ''.join(format(int(''.join(linha), 2), 'X') for linha in matriz)

    def calcularXORMatrizes(self, matriz1, matriz2):
        # Realiza operação XOR elemento a elemento entre duas matrizes 4x4 de elementos de 2 bits
        return [[format(int(matriz1[i][j], 2) ^ int(matriz2[i][j], 2), '02b')
                 for j in range(4)] for i in range(4)]

    def stringHEXparaMatriz(self, stringHEX):
        # Usa stringHEXparaStringBinaria para converter a string hexadecimal para binário
        stringBinaria = self.stringHEXparaStringBinaria(stringHEX)
        # Divide a string binária em uma matriz 4x4 de elementos de 2 bits
        return [[stringBinaria[i+j:i+j+2] for j in range(0, 8, 2)] for i in range(0, 32, 8)]

    def comprimirMatrizes(self, matrizes: list[list]):
        matriz = matrizes[0]
        for i in range(1, len(matrizes)):
            matriz = self.calcularXORMatrizes(matriz, matrizes[i])
        return matriz

    def stringParaMatrizes(self, string):
        stringBinaria = self.textoParaStringBinaria(string)
        stringBinaria = self.adicionarZerosNecessarios(stringBinaria)
        blocos = self.stringBinariaParaBlocos(stringBinaria)
        matrizes = []
        for bloco in blocos:
            matrizes.append(self.blocoParaMatriz(bloco))
        return matrizes

    def criptografarMatriz(self, matrizMensagem, matrizChave):
        # (Implementar após as outras funções)
        chave0 = matrizChave
        chave1 = self.dnl0(chave0)
        chave2 = self.dnl0(chave1)
        chave3 = self.dnl0(chave2)
        chave4 = self.dnl0(chave3)
        pass

    def descriptografarMatriz(self, matrizCriptografada):
        # (Implementar após as outras funções)
        pass

    def criptografar(self, mensagem, chave):
        # (Implementar após as outras funções)
        pass
    
    def descriptografar(self, criptografado, chave):
        # (Implementar após as outras funções)
        pass
    
    def exibirMatriz(self, matriz):
        # (Apenas para debug)
        print('+-----------+')
        for linha in matriz:
            print('|',end='')
            for byte in linha:
                print(byte, end='')
                print('|',end='')
            print('')
        print('+-----------+')
