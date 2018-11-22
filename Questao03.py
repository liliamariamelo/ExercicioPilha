print("O valor máximo da sua pilha é 7")
class Pilha():
#Construtor

  def __init__(self):
    self.pilha = []
    self.atingiu_maximo = 0

#Adciona Um Elemento ao Topo da Pilha

  def Push(self):
    elemento = int(input("Digite o Elemento a Ser Adcionado: "))
    if len(self.pilha) == 7:
      print("Sua Pilha já Atingiu o Tamanho Máximo!")
      self.atingiu_maximo = 1

    if self.atingiu_maximo == 0:
      self.pilha.append(elemento)

    self.atingiu_maximo = 0 
    print("Sua Pilha:",self.pilha)

#Retira Um Elemento do Topo da Pilha
  
  def Pop(self):
    if (len(self.pilha)==0):
      print("Não Há Elementos na Sua Pilha!")
    else:  
      self.pilha.pop()
      print("Sua Pilha Agora é",self.pilha)

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
p.Push()
print(p.pilha)
