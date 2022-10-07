from datetime import datetime

def bubble_sort(data):
  lst = list(data)
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
          lst[j], lst[i] = lst[i], lst[j]
  return lst

itens = [4,1,5,3,2]
sortItens = bubble_sort(itens)

print("Lista embaralhada:", itens)
print("Lista Ordenada:",sortItens)

#Criando um teste
itens = list(range(1,200))
itens[5], itens[6] = itens[6], itens[5]
count = 1000
start = datetime.now()

for n in range(1, count):
  bubble_sort(itens)

delta = datetime.now() - start
total_tempo = delta.seconds * 1000000 + delta.microseconds

print("Tempo total:", total_tempo)
