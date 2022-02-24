'''
    Modulo 1: Fundamentos em Pyrhon
            Desafio

    Objetivos:
            Exercitar os conceitos trabalhados no Modulo:
            Lacos de repeticao;
            Funcao range;
            funcao;
            Instalacao, importacao de modulos e pacotes. 
             
'''

#Bilbiotecas e pacotes utilizados
import pandas as pd

# Criando funcao

fun_soma1 = lambda x, y: x + y

def fun_soma2(x, y):
    print( x + y)


#crindo um laco de repeticao

num=0
while num < 11:
    print(num)
    num+=1


for i in range(1,101):
    print(i)

