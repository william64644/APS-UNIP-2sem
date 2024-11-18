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

s = SES()

chave = "1234"
mensagem = "Mensagem secreta aqui"
print(f"Mensagem Original:\n\t{mensagem}")

criptografado = s.criptografar(mensagem, chave)
print(f"Mensagem Criptografada:\n\t{criptografado}")

descriptografado = s.descriptografar(criptografado, chave)
print(f"Mensagem Descriptografada:\n\t{descriptografado}")