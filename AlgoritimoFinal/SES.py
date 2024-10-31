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
    estado = [[]]
    
    chaveMatriz = []
    chave1 = [[]]
    chave2 = [[]]
    chave3 = [[]]
    chave4 = [[]]
    
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
        # Exemplo: "abcd" -Retorna-> "01100001011000100110001101100100"
        pass

    def stringBinariaParaTexto(self, stringBinaria):
        # Exemplo: "01100001011000100110001101100100" -Retorna-> "abcd"
        pass
    
    def adicionarZerosNecessarios(self, stringBinaria):
        # Exemplo: "011000010110001001100011" -Retorna-> "00000000011000010110001001100011"
        # O comprimento da string binária retornada deve ser um múltiplo de 32
        # Adicione quantos zeros à esquerda forem necessários para isso
        pass
    
    def removerZerosNecessarios(self, stringBinaria):
        # Exemplo: "00000000011000010110001001100011" -Retorna-> "011000010110001001100011"
        # Dica: remover os primeiros 8 bits enquanto os primeiros 8 bits forem iguais a '00000000'
        pass

    def stringBinariaParaBlocos(self, stringBinaria):
        # Exemplo: "0110000101100010011000110110010001100101011001100110011101101000"
        # -Retorna-> ["01100001011000100110001101100100", "01100101011001100110011101101000"]
        # (Retornar a string binária dividida em blocos de 32 bits)
        pass
    
    def blocoParaMatriz(self, bloco):
        # Exemplo: "01100011011001000011000100110010" -Retorna-> [['01', '10', '00', '11'],
        #                                                         ['01', '10', '01', '00'],
        #                                                         ['00', '11', '00', '01'],
        #                                                         ['00', '11', '00', '10']]
        pass

    def matrizParaBloco(self, matriz):
        # Exemplo: [['01', '10', '00', '11'], -Retorna-> "01100011011001000011000100110010"
        #          ['01', '10', '01', '00'],
        #          ['00', '11', '00', '01'],
        #          ['00', '11', '00', '10']]
        pass

    def matrizParaStringHEX(self, matriz):
        # Exemplo:
        # [['01', '00', '00', '10'],
        # ['11', '01', '10', '10'],
        # ['10', '01', '11', '10'],
        # ['11', '10', '11', '01']] -Retorna-> "42DA9EED"
        pass

    def calcularXORMatrizes(self, matriz1, matriz2):
        pass

    def stringHEXparaMatriz(self, stringHEX):
        # Exemplo:
        # "42DA9EED" -Retorna-> [['01', '00', '00', '10'],
        #                       ['11', '01', '10', '10'],
        #                       ['10', '01', '11', '10'],
        #                       ['11', '10', '11', '01']]
        pass

    def criptografarMatriz(self, matrizMensagem):
        # (Implementar após as outras funções)
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



