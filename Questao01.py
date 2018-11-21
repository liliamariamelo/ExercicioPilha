class Pilha():

    def__init__(self):
        self.pilha = []

    def push(self,valor):
        self.pilha.append (valor)

    def pop(self):
        if(not(self.isEmpty())):
            return self.pilha.pop ()

    def isEmpty (self):
        return len(self.pilha)==0

    def length (self):
        return len(self.pilha)

    def peek(self):
        if(not(self.isEmpty())):
            return self.pilha [-1]




    
