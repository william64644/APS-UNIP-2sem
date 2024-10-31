def matrizSheetsParaMatrixPython():
    
    matrizSheets = """00	11	00	11
10	01	01	00
01	10	11	01
10	01	10	10"""
    matrizSheets = matrizSheets.replace('\t', ' ')

    print('[', end='')
    for i, linhas in enumerate(matrizSheets.splitlines()):
        print(linhas.split(), end='')
        if i < 3:
            print(',')
    print(']')





matrizSheetsParaMatrixPython()