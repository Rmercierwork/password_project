from generation_caractere import GenerationCaractere
import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

l1 = []

for x in range(3):
  l1.append(GenerationCaractere.chiffre_aleatoire(0))
for x in range(4):
  l1.append(GenerationCaractere.majuscul_aleatoire(0))

l1= shuffle(l1)
print(l1)