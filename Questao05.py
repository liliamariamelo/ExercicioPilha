class Pilha():
#Construtor

  def __init__(self):
    self.pilha = []

#Adciona Um Elemento ao Topo da Pilha

  def Push(self,elemento):
    self.pilha.append(elemento)
    print("Sua Pilha Agora eh",self.pilha)

#Retira Um Elemento do Topo da Pilha
  
  def Pop(self):
    if (len(self.pilha)==0):
      print("Não Há Elementos na Sua Pilha!")
    else:  
      self.pilha.pop()
      print("Sua Pilha Agora eh",self.pilha)

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

  def Clear(self):
    self.pilha = []  

print("LETRA A")
print("\n")    
#Letra A 
p = Pilha()
for i in range(16):
  if i % 3 == 0:
    p.Push(i)

p.Clear()

print("\n")
print("LETRA B")
print("\n")
#Letra B 

for i in range(16):
  if i % 3 == 0:
    p.Push(i)
  elif i % 4 == 0:
    p.Pop()
