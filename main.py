#Coleta de dois números binários;
binario_0 = input('Digite o primeiro número binário: ')
binario_1 = input('Digite o segundo número binário: ')

#Cria uma lista para armazenar o resultado da soma;
resultado = []

#A variável carry é utilizada para armazenar o valor que será transportado para a próxima casa binária;
carry = 0

#Ordena os calores recebidos em um array;
array_0 = list(binario_0)
array_1 = list(binario_1)

#Verifica o tamanho dos arrays;
tamanho_0 = len(array_0)
tamanho_1 = len(array_1)

#Verifica se há diferença entre os tamanhos dos arrays;
diferenca = abs(tamanho_0 - tamanho_1)

#Se houver diferença, adiciona zeros à esquerda do array menor;
if tamanho_0 > tamanho_1:
    for i in range(diferenca):
        
        # Adiciona zeros à esquerda do array 1;
        array_1.insert(0, '0')
elif tamanho_0 < tamanho_1:
    for i in range(diferenca):
        
        # Adiciona zeros à esquerda do array 0;
        array_0.insert(0, '0')

#Verifica a operação aritmética a ser realizada;
operacao = input('Digite a operação [ + , - , * , / ]: ')

#Cria um contador que será utilizado para percorrer os arrays, o contador começa no último elemento do array e vai até o primeiro. Não importa o tamanho do array_0, pois os arrays são de tamanhos iguais nesse ponto;
cont= len(array_0) - 1

#Se a operação for soma[+], o código abaixo será executado;
if operacao == '+':
    
    #Repete o loop enquanto o contador i for menor que o tamanho do array_0, o loop irá percorrer os dois arrays simultaneamente, somando os valores binários e armazenando o resultado na lista resultado;
    for i in range(len(array_0)):
        if ((array_0[cont] == array_1[cont] == '0' )and carry == 0):
            
            #Insere o valor '0', na posição 0 da lista resultado;
            resultado.insert(0, '0')
            cont = cont - 1
            carry = 0         
        elif ((array_0[cont] == array_1[cont] == '0') and carry == 1 ):
            resultado.insert(0, '1')
            cont = cont - 1
            carry = 0
        elif ((array_0[cont] == array_1[cont] == '1') and carry == 0):
            if(i == (len(array_0)-1)):
                resultado.insert(0, '11')
            else:
                resultado.insert(0, '0')
                cont = cont - 1
                carry = 1
        elif ((array_0[cont] == array_1[cont] == '1') and carry == 1):
            if(i == (len(array_0)-1)):
                resultado.insert(0, '11')
            else:
                resultado.insert(0, '1')
                cont = cont - 1
                carry = 1     
        elif ((array_0[cont] != array_1[cont]) and carry == 1):
            if (i == (len(array_0)-1)):
                resultado.insert(0, '10')
            else:
                resultado.insert(0, '0')
                cont = cont - 1
                carry = 1
        elif ((array_0[cont] != array_1[cont]) and carry == 0):
            resultado.insert(0, '1')
            cont = cont - 1
            carry = 0
else:
    print('Operação não implementada ainda.')
    
   		
resultadocompleto = ''.join(resultado)
print(resultadocompleto)
