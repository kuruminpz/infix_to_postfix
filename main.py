from function import *

print("\tINFIXA para PÓS-FIXA\n")
print("DICA: Não use espaços e sempre use parenteses.")

infixa = input("Digite a Função infixa: ")

posfixa = postfix(infixa)

# teste: (((2+3)*(4+5))+((3+7)*(4+2)))*((2+3)*(5+7))

print(infixa)
print(posfixa)
final = calcular(posfixa)
print(f"A resposta é: {final}")

