#import math 
#diametro = float(input('diametro:'))
#raio = diametro / 2
#area = 2 * raio * math.pi
#print (f'area = {round(area, 1)}')

#import math
#a=float (input('base'))
#b= float (input('altura'))
#if b == float('0'):
#    print ('fim')
#else:
#    hipoten = math.sqrt(a**2+b**2)
#
#print (f'a hipotenusa é {round(hipoten,1)} ')

#a = float(input('primeiro numero: '))
#b = float(input('segundo numero:'))
#op = input('sinal')
#if op == '+':
#    result = a + b
#elif op == '-':
#    result = a - b
#elif op == '/':
#    result = a / b
#elif op == '*':
#    result = a * b#

 #   print (round(result,2))
#lse: 
#   print (f' operacao {op} não valida')

#peso = float(input('qual o seu peso? '))
#unidade = input('kg ou lb?')
#if unidade == 'kg': 
#    peso = peso * 2
#    un = 'lbs'
#    print (f'seu peso é: {peso} {un}')
#elif unidade == 'lb':
#    peso = peso / 2
#    un = 'kg'
#    print (f'seu peso é: {peso} {un}')

#else: 
#    print (f' {unidade} é uma unidade desconhecida')
#num = float(input ('numero: '))
#print ('positivo' if num > 0 else 'negativo')
#if num > 0:
#    print ('positivo')
#else:
#    print ('negativo')
#print ('par' if num % 2 == 0 else 'impar')
#nome = input('nome: ')
#resultado = len(nome)
#if resultado > 5:
#    print('2avfjdknvjkd')
#else:
#    print (resultado)
#resultado = nome.find('a')
#print ('njfdnvhjfnbhjfg' if resultado > 5 else 'menor')


#telefone= input ('telefone: ')
#telefone = telefone.replace('-', '')
#print (telefone)

#usuario = input ('usuario: ')

#if len(usuario) > 12:
#if caracteres < 12:
#      print ('muito grande')

#elif not usuario.find (' ') == -1:
#    print ('tem espaço')

#elif not usuario.find ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') == -1:
#elif not usuario.isalpha():
#     print ('tem numero')

#else:
    
#
#     print ('ok')
#cartao = '123456789012345'
#print (cartao[ :10:2])
#valor_1 = 12345.6789
#print (f" o valor 1 é {valor_1:.3f} ")
#nome = input ('insura o seu nome')
#while nome == '':
#    print ('nome vazio')
#    nome = input ('insura o seu nome')
#print (f' seu nome é {nome}')
#numero = int (input ('insura um numero de 0-10: '))
#while numero < 0 or numero > 10:
#   print ('numero invalido')
#    numero = int (input ('insura um numero de 1-10 cazzo '))
#print (f' seu numero é {numero}') 
#inic = float (input ('insira o valor inicial: '))
#juros = float (input ('insura a taxa de juros: '))
#mes = int (input ('insura o numero de meses: '))

#while inic == 0: 
#    print ('valor inicial invalido')
#    inic = float (input ('insura o valor inicial: '))

#fim = inic * (1+ juros/100) ** mes
#print (f' (o valor final é {fim:.2f} dinheiros.)')
#import time 
#t=10
#while t > 0:
#    print (t)
#    time.sleep (1)
#    t = t-1

#print ('fim')
#linhas = int (input ('quantas linhas? '))
#colunas = int (input ('quantas colunas? '))
#simbulo = input ('qual simbulo? ')

#or abc in range (linhas):
#    for abc in range (colunas):
#        print (simbulo, end=' ')
#    print ()
    
        
#print ('fim do programa')
   

#frutas = {'maçã', 'banana', 'laranja', 'uva', 'pera', 'banana'}
#for fruta in frutas: 
#print (frutas)

#comidas = []
#precos = [] 
#total = ()
##while True:
#    comida = input ('qual comida ira comprar? (aperte q para sair) ')
#    if comida.lower() == 'q':
#        break 
#    else: 
#        preco = float (input (f'qual o preço da {comida}? '))
#        comidas.append (comida)
#        precos.append (preco)#

#for comida in comidas: 
#    print (f' voce comprou: {comida}')

#total = sum (precos)#
#print (f' o total gasto foi {total:.2f}')
#print ('fim do programa')

#vegetais = ('cenoura', 'batata', 'alface', 'tomate' )
#frutas = ('maçã', 'banana', 'laranja', 'uva' )
#carnes = ('frango', 'carne bovina', 'porco' )

#comidas = [vegetais, frutas, carnes ]

#print (comidas)
#digitos = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ('#',0,'*'))

#for linha in digitos: 
#    for numero in linha: 
#        print (numero, end=' ')      
#    print ()     
#---------------------------------------------------------------------------------------------
#perguntas = ('quantos elementos tem na tabela periodica? ',
#              'qual o maior planeta do sistema solar? ',
#              'qual a capital da frança? ',
#              'qual o elemento quimico representado por O? ',
#              'quem escreveu dom casmurro? ')#
#opcoes = (('A:1', 'B:2', 'C:correto', 'D:4' ),
         # ( 'a','b', 'c', 'd' ),
#          ('A:mercurio', 'B:venus', 'C:jupiter', 'D:terra' ),
#          ('A:paris', 'B:roma', 'C:londres', 'D:madri' ),
#          ('A:hidrogenio', 'B:oxigenio', 'C:nitrogenio', 'D:sodio' ),
#          ('A:machado de assis', 'B:jorge amado', 'C:joao guimaraes rosa', 'D:maria quiteria' )) 

#respostas = ('c', 'c', 'a', 'b', 'a')
#chutes = []
#pontuacao = 0
#numero_da_questao = 0


#for pergunta in perguntas:
#    print ('-------------------------------')
#    print (pergunta)
#    for opcao in opcoes [numero_da_questao]:
#        print (opcao)
#    chute = input ('sua resposta: ').lower()
#    chutes.append (chute)
#    if chute == respostas [numero_da_questao]:
#        pontuacao += 1
#        print ('correto!')
#    else: 
#        print ('incorreto!')
#        print (f'a resposta correta é {respostas [numero_da_questao ]}')#
#    numero_da_questao += 1

#print ('-------------------------------')
#print ('resultados: ')
#print ('-------------------------------')
#print ('respostas: ', end='') 
#for resposta in respostas:
#    print (resposta, end=' ')
#print ()

#print ('chutes: ', end='') 
#for chute in chutes:
#    print (chute, end=' ')
#print ()

#pontuacao = pontuacao / len(perguntas) * 100
#print (f'sua pontuação foi de {pontuacao} %')
#---------------------------------------------------------------------------------------------


#menu = {'1-a': 8.00,
#        '2-b': 20.00,
#        '3-c': 4.00,
#        '4-d': 6.00,   
#        '5-e': 7.00}

#pedido = []
#total = 0

#for item, valor in menu.items():
#    print (f' {item:15}: R$ {valor:.2f}')

#while True:
#    comida = input ('o que deseja? (aperte q para sair): ')
#    if comida.lower() == 'q':
#        break
#    elif menu.get(comida) is not None:
#        pedido.append (comida)

#for comida in pedido: 
#    total = total + menu.get(comida)
#    print (comida, end=', ')
#print ()
#print (f'o total do seu pedido é R$ {total:.2f}')

#import random

#numero = random.randint (1, 5)
#rodando = True
#chute = 0
##print ('adivinhe um numero entre 1 e 5')
#while rodando:
#    tentativa = input ('deseja tentar adivinhar o numero? ')
#    tentativa = int(tentativa)
    
#    chute += 1
#    if tentativa == numero: 
#        break
#    elif tentativa > numero:
#        print ('muito alto')
#    elif tentativa < numero:
#        print ('muito baixo')
#    elif tentativa < 5 and tentativa > 1:
#        print ('numero invaloido')

#print (f'o numero era: {numero}')
#print (f'numero de tentativas: {chute}')

import random 

opcoes = ['pedra', 'papel', 'tesoura']
rodando = True

while rodando:
    pc =random.choice(opcoes)
    tentativa = input ('escolha pedra, papel ou tesoura: ').lower()

    while tentativa not in opcoes:
        print (f'{tentativa} é uma opção invalida')
        tentativa = input ('escolha pedra, papel ou tesoura: ').lower()

    if tentativa == pc: 
        print ( f'{tentativa} e {pc}, empate')
        
    elif (tentativa == 'pedra' and pc == 'tesoura') or (tentativa == 'papel' and pc == 'pedra') or (tentativa == 'tesoura' and pc == 'papel'):
        print (f'{tentativa} e {pc}, voce ganhou')
    else:
        print (f'{tentativa} e {pc}, pc ganhou')
    
    print ('jogar novamente? s/n')
    resposta = input ().lower()
    if resposta == 'n':
        rodando = False