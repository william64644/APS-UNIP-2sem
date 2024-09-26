"""
O experimento revelou que esse algorítimo irá reverter o processo de criptografia ao criptografar a sua saída com a mesma chave
"""

data = []
keys = []
intermediates = [0]*16
results = [0]*16

for k in range(4):
    for l in range(4):
        binary = format(l, '02b')

        data.append(binary)
print()

for i in range(4):
    for j in range(4):
        binary = format(i, '02b')

        keys.append(binary)
print()
print("Data:")
print(data)
print("Keys:")
print(keys)

def XOR(word1, word2):
    if word1 == "00" and word2 == "00":
        return "00"
    elif word1 == "00" and word2 == "01":
        return "01"
    elif word1 == "00" and word2 == "10":
        return "10"
    elif word1 == "00" and word2 == "11":
        return "11"
    elif word1 == "01" and word2 == "00":
        return "01"
    elif word1 == "01" and word2 == "01":
        return "00"
    elif word1 == "01" and word2 == "10":
        return "11"
    elif word1 == "01" and word2 == "11":
        return "10"
    elif word1 == "10" and word2 == "00":
        return "10"
    elif word1 == "10" and word2 == "01":
        return "11"
    elif word1 == "10" and word2 == "10":
        return "00"
    elif word1 == "10" and word2 == "11":
        return "01"
    elif word1 == "11" and word2 == "00":
        return "11"
    elif word1 == "11" and word2 == "01":
        return "10"
    elif word1 == "11" and word2 == "10":
        return "01"
    elif word1 == "11" and word2 == "11":
        return "00"

def XNOR(word1, word2):
    if word1 == "00" and word2 == "00":
        return "11"
    elif word1 == "00" and word2 == "01":
        return "10"
    elif word1 == "00" and word2 == "10":
        return "01"
    elif word1 == "00" and word2 == "11":
        return "00"
    elif word1 == "01" and word2 == "00":
        return "10"
    elif word1 == "01" and word2 == "01":
        return "11"
    elif word1 == "01" and word2 == "10":
        return "00"
    elif word1 == "01" and word2 == "11":
        return "01"
    elif word1 == "10" and word2 == "00":
        return "01"
    elif word1 == "10" and word2 == "01":
        return "00"
    elif word1 == "10" and word2 == "10":
        return "11"
    elif word1 == "10" and word2 == "11":
        return "10"
    elif word1 == "11" and word2 == "00":
        return "00"
    elif word1 == "11" and word2 == "01":
        return "01"
    elif word1 == "11" and word2 == "10":
        return "10"
    elif word1 == "11" and word2 == "11":
        return "11"

"""
key -> method
0 - XOR XOR
1 - XOR XNOR
2 - XNOR XOR
3 - XNOR XNOR
"""
i = 0
j = 0
for i in range(16):
    opcode = i%4
    if opcode == 0:
        intermediates[i] = XOR(data[i], keys[i])
        results[i] = XOR(keys[i], intermediates[i]) 
    elif opcode == 1:
        intermediates[i] = XOR(data[i], keys[i])
        results[i] = XNOR(keys[i], intermediates[i]) 
    elif opcode == 2:
        intermediates[i] = XNOR(data[i], keys[i])
        results[i] = XOR(keys[i], intermediates[i]) 
    elif opcode == 3:
        intermediates[i] = XNOR(data[i], keys[i])
        results[i] = XNOR(keys[i], intermediates[i])
print("Results 1:")
print(results)

data = results

i = 0
j = 0
for i in range(16):
    opcode = i%4
    if opcode == 0:
        intermediates[i] = XOR(data[i], keys[i])
        results[i] = XOR(keys[i], intermediates[i]) 
    elif opcode == 1:
        intermediates[i] = XOR(data[i], keys[i])
        results[i] = XNOR(keys[i], intermediates[i]) 
    elif opcode == 2:
        intermediates[i] = XNOR(data[i], keys[i])
        results[i] = XOR(keys[i], intermediates[i]) 
    elif opcode == 3:
        intermediates[i] = XNOR(data[i], keys[i])
        results[i] = XNOR(keys[i], intermediates[i])
        
print("Results 2:")
print(results)
