# Эта программа шифрует слово на основе шифра Виженера
#                               Оберган Татьяна
# al - алфавит
# sl - шифруемое слово
# sh - шифр
# za - зашифрованное слово
al = ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
      'p','q','r','s','t','u','v','w','x','y','z']
za = []
sl = list(input('Введите шифруемое слово: ').lower())
sh = list(input('Введите шифр: ').lower())
#продление шифра
if len(sh) < len(sl):
    for i in range(len(sl)-len(sh)):
        sh.append(sh[i])
#шифрование
for i in range(len(sl)):
    a = ((al.index(sl[i]) + al.index(sh[i]))%26) - 1
    za.append(al[a])
#вывод
for i in za:
    print(i,end='')