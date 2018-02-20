names = input('Станции ').split(' ')
cords = input('Кординаты ').replace('(','').replace(')', '').replace(',','').split(' ')
print(len(names), len(cords))

s = []
for i in range(len(names)):
    m = [names[i], (int(cords[i*2]), int(cords[i*2 + 1]))]
    s.append(m)
print(s)











