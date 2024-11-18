"""
Esse é o programa utilizado para usar o módulo SES na prática

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