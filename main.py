primeiro_binario = input("Digite o primeiro número binário: ")
segundo_binario = input("Digite o segundo número binário: ")

tamanho_primeiro = 0
tamanho_segundo = 0

resultado = []
carry = 0

array1 = list(primeiro_binario)
array2 = list(segundo_binario)

tamanho_primeiro = len(array1)
tamanho_segundo = len(array2)

diferenca = abs(tamanho_primeiro - tamanho_segundo)

if tamanho_primeiro > tamanho_segundo:
    for i in range(diferenca):
        array2.insert(0, '0')
elif tamanho_primeiro < tamanho_segundo:
    for i in range(diferenca):
        array1.insert(0, '0')

operacao = input("Digite a operação [ + , - , * , / ]: ")

cont= len(array1) - 1

if operacao == '+':
    for i in range(len(array1)):
        if ((array1[cont] == array2[cont] == '0' )and carry == 0):
            resultado.insert(0, "0")
            cont = cont - 1
            carry = 0         
        elif ((array1[cont] == array2[cont] == '0') and carry == 1 ):
            resultado.insert(0, '1')
            cont = cont - 1
            carry = 0
        elif ((array1[cont] == array2[cont] == '1') and carry == 0):
            resultado.insert(0, "0")
            cont = cont - 1
            carry = 1
        elif ((array1[cont] == array2[cont] == '1') and carry == 1):
            if(i == (len(array1)-1)):
                resultado.insert(0, "11")
            else:
                resultado.insert(0, "1")
                cont = cont - 1
                carry = 1     
        elif ((array1[cont] != array2[cont]) and carry == 1):
            if (i == (len(array1)-1)):
                resultado.insert(0, "10")
            else:
                resultado.insert(0, "0")
                cont = cont - 1
                carry = 1
        elif ((array1[cont] != array2[cont]) and carry == 0):
            resultado.insert(0, "1")
            cont = cont - 1
            carry = 0
print(array1)
print(array2)     		
resultadocompleto = ''.join(resultado)
print(resultado)