"""
CARACTERÍSTICAS DO ALGORÍTIMO
criptografia simétrica
256 bits de criptografia
dupla verificação de integridade 
"""
# PROCESSO DE CRIPTOGRAFAR
def criptografar(mensagem, chave):
    # 1 - defina bruto para uma string da mensagem convertida para código binário
    bruto = ''.join(format(ord(i), '08b') for i in mensagem)
    # 2 - defina r256 para o resto da divisão do comprimento de bruto por 256
    
    # 3 - defina comprimentoPadding para 256 - r256
    # 4 - adicione '0' * comprimentoPadding no final da string bruto
    # 5 - defina paddingLenghtBinary para comprimentoPadding convertido para binário adicionando zeros a esquerda suficientes para completar 256 bits de comprimento
    # 6 - adicione paddingLenghtBinary no final de bruto
    # 7 - defina words para bruto dividido em uma lista de partes iguais de 256 bits (itertools.batched(iterable, n))
    # 8 - defina N para o comprimento de words

"""
Operação de acordo com os 2 primeiros bits da chave
00 -> XOR XOR
11 -> XNOR XNOR
01 -> XOR XNOR
10 -> XNOR XOR


PROCESSO DE DESCRIPTOGRAFAR
"""