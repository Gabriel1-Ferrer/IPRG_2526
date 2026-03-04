llistanotes = [5, 7, 9, 4, 6, 3, 1, 8, 2, 10]

print(llistanotes)

[print(x) for x in llistanotes]

print ([x for x in range(11) if x > 4])

contador = 0


for nota in llistanotes:
  if nota >= 5: 
        contador = contador + 1
print(contador)

contador = 0

for nota in llistanotes:
    if nota < 5:
        contador += 1
print(contador)