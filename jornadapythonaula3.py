# -*- coding: utf-8 -*-
"""JornadaPythonAula3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bowRJfU7UBUQQhCG7Io8o_4kRspK2-x9
"""

nota1 = 5.0
nota2 = 4.8

def verificar_aprovacao():
    media = calcular_media([nota1, nota2])

    if media >= 6:
      print("O Aluno foi Aprovado")
    else:
      print("O Aluno foi Reprovado")


def calcular_media(notas):
    quantidade = len(notas)

    soma = 0
    for nota in notas:
        soma = soma + nota

    media = soma / quantidade

    return media

verificar_aprovacao()

