"""
Essse é o módulo onde são definidos os métodos necessários para o processo de criptografia e descriptografia.
"""
def hi():
    print("HI")
class SES:
        
    CARACTERES_POR_BLOCO = 4
    
    mensagem = ''
    mensagemBinario = ''
    
    estado = [[]] # Armazena o estado atual durante o processo de criptografia/descriptografia
    
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
    def dnl0(matriz):
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
    def dnl1(matriz):
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
    def dnl0reverso(matriz):
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
        matriz[1][2] = buffer

        return matriz

    # Recebe uma matriz e retorna o seu respectivo deslocamento não linear 1 invertido
    def dnl1reverso(matriz):
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
        matriz[1][1] = matriz[1][3]
        matriz[1][3] = matriz[0][0]
        matriz[0][0] = buffer

        return matriz
    
    
    def criptografarBloco(mensagem, chave):
        pass
    
    def descriptografarBloco(criptografado, chave):
        pass
    
    
    
    def criptografar(mensagem, chave):
        pass
    
    def descriptografar(criptografado, chave):
        pass
    

    def exibirMatriz(matriz):
        for linha in matriz:
            print('|',end='')
            for byte in linha:
                print(byte, end='')
                print('|',end='')
            print('')


