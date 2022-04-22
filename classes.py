class Node():
    def __init__(self, valor, prox = None):
        self.valor = valor
        self.prox = prox

    def __str__(self):
        return str(self.valor)

class Pilha():
    def __init__(self):
        self.top = None
        self.cont = 0

    def __str__(self):
        strPilha = ""
        node = self.top
        while True:
            strPilha += str(node.valor) + "\n"
            node = node.prox
            if node == None:
                break
        return strPilha

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, v):
        if self.isEmpty():
            self.top = Node(v)
            self.cont += 1
        else:
            novo = Node(v, self.top)
            self.top = novo
            self.cont += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia")
        v = self.top.valor
        self.top = self.top.prox
        self.cont -= 1
        return v

    def stacktop(self):
        if self.isEmpty():
            raise Exception("Pilha vazia")
        return self.top.valor

