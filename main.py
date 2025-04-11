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

#Verifica se há diferença entre os tamanhos dos arrays, a ultilização do módulo é necessária para o caso em que tamanho_0 é menor que tamanho_1;
diferenca = abs(tamanho_0 - tamanho_1)

#Se houver diferença, adiciona zeros à esquerda do array menor;
if tamanho_0 > tamanho_1:
    #Utiliza a 
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

#Se a operação for soma[ + ], o código abaixo será executado;
if operacao == '+':
    #Inicio um loop de repetição que considera o tamanho do array;
    for i in range(len(array_0)):
        #Estrutura condicional para definir os elementos o array resultado[]
        if ((array_0[cont] == array_1[cont] == '0' )and carry == 0):
            #Insere o valor '0' na posição 0 do array, isso porque preciso que os números sejam inseridos da esquerda para a direita, se fosse o inverso, usaria append;
            resultado.insert(0, '0')
            #Deduz o meu contador para que agora ele pegue o elemento anterior do array, já que a variável cont é usada para definir o índice do meu array;
            cont -= 1
        #O elif é usado para dar uma outra condição quando a anterior não é verdadeira;       
        elif ((array_0[cont] == array_1[cont] == '0') and carry == 1 ):
            #Insere o valor '1' na posição 0 do array;
            resultado.insert(0, '1')
            cont -= 1
            carry = 0
        elif ((array_0[cont] == array_1[cont] == '1') and carry == 0):
            #Temos outra condição para a inserção de valores no array resultado, na condição do if, verificamos se a rodada em que estamos é a ultima
            if(i == (len(array_0)-1)):
                resultado.insert(0, '10')
            else:
                resultado.insert(0, '0')
                cont -= 1
                carry = 1
        elif ((array_0[cont] == array_1[cont] == '1') and carry == 1):
            if(i == (len(array_0)-1)):
                resultado.insert(0, '11')
            else:
                resultado.insert(0, '1')
                cont -= 1
                carry = 1     
        elif ((array_0[cont] != array_1[cont]) and carry == 1):
            if (i == (len(array_0)-1)):
                resultado.insert(0, '10')
            else:
                resultado.insert(0, '0')
                cont -= 1
                carry = 1
        elif ((array_0[cont] != array_1[cont]) and carry == 0):
            resultado.insert(0, '1')
            cont -= 1
            carry = 0
#Aqui informo ao usuário sobre a indisponibilidade de outra operações até o momento;
else:
    print('Operação não implementada ainda.')
#Ness final, uno todos os elementos do array para formar a variável que será apresentada ao usuário; 		
resultadocompleto = ''.join(resultado)
print(resultadocompleto)
