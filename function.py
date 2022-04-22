from classes import *

def postfix(infix):
    p = Pilha()
    posfixa = []

    for i in range(len(infix)):
        c = infix[i]
        if c >= '0' and c <= '9' or c.lower() >= 'a' and c.lower() <= 'z':
            posfixa.append(c)
        elif isOperador(c):
            while not p.isEmpty() and prioridade(c, p.stacktop()):
                topo = p.pop()
                posfixa.append(t)
            p.push(c)
        elif c == '(':
            p.push(c)
        elif c == ')':
            while True:
                topo = p.pop()
                if topo != '(':
                    posfixa.append(topo)
                else:
                    break
    while not p.isEmpty():
        posfixa.append(p.pop())

    posfixa = "".join(posfixa)

    return posfixa

def operacao(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    else:
        return False  # Retorna False caso o operando não seja válido

def avaliarPosfixa(expressao):
    """ Avalia uma expressao posfixa"""
    p = Pilha()
    for i in range(len(expressao)):
        c = expressao[i]
        if c >= "0" and c <= "9":
            p.push(c)
        else:
            opnd2 = p.pop()
            opnd1 = p.pop()

            valor = operacao(c, int(opnd1), int(opnd2))

            if valor:  # Verifica se o operando é válido
                p.push(valor)
            else:
                return "Operador invalido"

    resultado = p.pop()

    if p.isEmpty():  # Verifica se ao final a pilha está vazia
        return resultado
    else:
        return "Expressao invalida"

def isOperador(s):
    if s == "+" or s == "-" or s == "*" or s == "/":
        return True
    else:
        return False

def prioridade(c, t):
    """Verifica a prioridade entre os operandos"""

    if c == '*' or c == '/':
        prio_c = 2
    elif c == '+' or c == '-':
        prio_c = 1
    else:
        prio_c = 4

    if t == '*' or t == '/':
        prio_t = 2
    elif t == '+' or t == '-':
        prio_t = 1
    else:
        prio_t = 0

    return prio_c <= prio_t

def calcular(pos):
    pilha2 = Pilha()

    for i in range(len(pos)):
        carac = pos[i]
        if carac >= "0" and carac <="9":
            pilha2.push(carac)
        else:
            try:
                unit1 = int(pilha2.pop())
                unit2 = int(pilha2.pop())
            except AttributeError:
                print("Operador sobrando na Expressão")
                exit()
            result = operacao(carac,unit1,unit2)

            if result:
                pilha2.push(result)
            else:
                return "Operador Inválido"
    resposta = pilha2.pop()
    if pilha2.isEmpty():
        return resposta
    else:
        return "Expressão Inválida"

