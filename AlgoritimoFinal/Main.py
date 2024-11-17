"""
Esse é o programa que será utilizado para usar o módulo SES na prática

Exemplo de uso hipotético:

from SES import SES as s

mensagem = "ab21"
chave = "cd12"

criptografado = s.criptografar(mensagem, chave)
print(criptografado) # Exibe: 42DA9EED

descriptografado = s.descriptografar(criptografado, chave)
print(descriptografado) # Exibe: ab21
"""

from SES import SES
# Usar deepcopy para passar parametros das funções por que o python passa as listas por referência e não por valor
# Exemplo: s.chave1 = s.dnl0(deepcopy(s.chave0))
from copy import deepcopy

s = SES()

chave = "as"
mensagem = "asad: as\n"

crip = s.criptografar(mensagem, chave)

print(crip)

decrip = s.descriptografar(crip, chave)
print(list(decrip))
