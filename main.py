"""
CARACTERÍSTICAS DO ALGORÍTIMO
criptografia simétrica
256 bits de criptografia
dupla verificação de integridade 

PROCESSO DE CRIPTOGRAFAR
1 - defina bruto para uma string dos dados de entrada convertidos para código binário
2 - defina r256 como o resto da divisão do comprimento de bruto por 256
3 - defina comprimentoPadding para 256 - r256
4 - adicione '0' * comprimentoPadding no final da string bruto
5 - defina paddingLenghtBinary para comprimentoPadding convertido para binário adicionando zeros a esquerda suficientes para completar 256 bits de comprimento
6 - adicione paddingLenghtBinary no final de bruto
7 - defina words para bruto dividido em uma lista de partes iguais de 256 bits



PROCESSO DE DESCRIPTOGRAFAR
"""