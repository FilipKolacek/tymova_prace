import random

barvy = ["červená", "zelená", "modrá"]
cisla = [1,2,3,4]

barvy.append("fialová")

for i in barvy:
    print(i)

nahodnaHodnota = random.choice(barvy)
print(nahodnaHodnota)
