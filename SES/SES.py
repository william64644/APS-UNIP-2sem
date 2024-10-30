CARACTERES_POR_BLOCO = 4

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
    matriz[1][3] = matriz[1][1]
    matriz[1][1] = matriz[2][2]
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

# Recebe uma matriz e retorna o seu respectivo deslocamento não linear 1 invertido
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

# Recebe uma matriz e retorna o seu respectivo deslocamento não linear 0 invertido
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


