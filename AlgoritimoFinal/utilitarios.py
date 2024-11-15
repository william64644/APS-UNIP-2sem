"""
Funções usadas exclusivamente para facilitar algumas etapas do desenvolvimento
"""


def matrizSheetsParaMatrizPython():
    
    matrizSheets = """01	10	00	11
01	10	01	00
00	11	00	01
00	11	00	10"""
    matrizSheets = matrizSheets.replace('\t', ' ')

    print('[', end='')
    for i, linhas in enumerate(matrizSheets.splitlines()):
        print(linhas.split(), end='')
        if i < 3:
            print(',')
    print(']')


matrizSheetsParaMatrizPython()
