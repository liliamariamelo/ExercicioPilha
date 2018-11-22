class Pilha():n
#Construtor

  def __init__(self):
    self.pilha = []
    self.tem = 0

#Adciona Um Elemento ao Topo da Pilha


  def Push(self):    
    elemento = int(input("Digite o elemento a ser adcionado:"))
    for i in range(len(self.pilha)):
      if elemento == self.pilha[i]:
        print("Ops.. Esse elemento já existe em sua Pilha!")
        self.tem = 1
      
    if self.tem == 0:
      self.pilha.append(elemento)
    
    self.tem = 0
    print("Sua Pilha:",self.pilha)

#Retira Um Elemento do Topo da Pilha
  
  def Pop(self):
    if (len(self.pilha)==0):
      print("Não Há Elementos na Sua Pilha!")
    else:  
      self.pilha.pop()
      print("Sua Pilha",self.pilha)

#Verifica se a Pilha está Vazia
  
  def IsEmpty(self):
    if len(self.pilha) == 0:
      print("Sua Pilha Esta Vazia")
    else:
      print("Sua Pilha Contem Elementos")

#Verifica o Topo da Pilha
  
  def Peek(self):
    topo = self.pilha[-1]
    print("O Topo da Pilha é o",topo)

#Verifica o Tamanho da Pilha  
  def Length(self):
    tamanho = (len(self.pilha))
    if tamanho >1:
      print("Sua Pilha Contem %d Elementos"%(tamanho))
    elif tamanho ==1:
      print("Sua Pilha Contem 1 Elemento!")
    else:
      print("Sua Pilha Não Contem Nenhum Elemento!")

p = Pilha()
p.Push()
p.Push()
p.Push()
p.Push()
p.Push()
p.Push()
p.Push()

print(p.pilha)
