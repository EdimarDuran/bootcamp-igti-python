'''
    Modulo 1: Fundamentos em Pyrhon
            Trabalho Pratico

    Objetivos:
            Exercitar os conceitos trabalhados no Módulo:
            Criacao de variaveis em Python.
            Tipos de variaveis em Python (String, Float, Integral, Boolean).    
            Formas de armazenamento em Dados (List, Tuple, Sets, Dictionary). 
'''

var_1= ('Uva', 'Abacate', 'larnaja', 'melancia')
var_2= [2.1,25.2,35.1,85.5,21.5]
var_3 = {'MG':31, 'SP':35, 'RJ':33, 'ES':32}

# craiacao de uma variavel que contem os tipos das variaveis: 

tip_var_1 = type(var_1)
tip_var_2 = type(var_2)
tip_var_3 = type(var_3)

print("As variaveis var_1, var_2, var_3, sao respectivamente do tipo {}, {}, {}".format(tip_var_1,tip_var_2,tip_var_3))