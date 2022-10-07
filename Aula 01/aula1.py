from datetime import datetime

def bubble_sort(data):
  lst = list(data)
  for i in range(len(lst)):
    for j in range(i+1, len(lst)):
      if lst[j], lst[i] = lst[i], lst[j]
  return lst

itens = [4,1,5,3,2]
sortItens = bubble_sort(itens)

print(itens)
print(sortItens)
