decimal_digitado = int(input("Digite um número em decimal: "))
decimal = decimal_digitado
binario = []
if decimal == 0:
    print(decimal)
else:
    while decimal > 1:
        bit = decimal % 2
        binario.insert(0, bit)
        decimal = decimal // 2
    if decimal == 1:
        binario.insert(0, decimal)
    print(f" O binário do número {decimal_digitado} é igual a: {"".join(map(str, binario))}")