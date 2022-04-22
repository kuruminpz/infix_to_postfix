from function import *

print("\tINFIXA para PÓS-FIXA\n")
print("DICA: Não use espaços e sempre use parenteses.")

infixa = input("Digite a Função infixa: ")

posfixa = postfix(infixa)

print(infixa)
print(posfixa)