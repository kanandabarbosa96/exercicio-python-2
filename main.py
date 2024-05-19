#Faça um programa que solicite ao usuário um número inteiro e exiba todos os pares de 0 até o número fornecido.

num = int(input("Digite um numero: "))

for i in range (num+1):
    if i % 2 == 0:
        print(i)