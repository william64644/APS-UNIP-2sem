import from main import *

# Using the standart of 0=success and 1=failure from the C language

def tAlternar00(data = "aaaaaaaabbbbbbbb"):
    result = alternar00(data)
    if result == "bbbbbbbbaaaaaaaa":
        return 0
    else:
        return 1

def tAlternar01(data = "aaaabbbbaaaabbbb"):
    result = alternar00(data)
    if result == "bbbbaaaabbbbaaaa":
        return 0
    else:
        return 1

def tAlternar10(data = "aabbaabbaabbaabb"):
    result = alternar00(data)
    if result == "bbaabbaabbaabbaa":
        return 0
    else:
        return 1

def tAlternar00(data = "abababababababab"):
    result = alternar00(data)
    if result == "babababababababa":
        return 0
    else:
        return 1

print(f"Teste alternar 00: {tAlternar00()}")
print(f"Teste alternar 01: {tAlternar01()}")
print(f"Teste alternar 10: {tAlternar10()}")
print(f"Teste alternar 11: {tAlternar11()}")