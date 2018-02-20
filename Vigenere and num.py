# Эта программа шифрует слово на основе шифра Виженера
#                               Оберган Татьяна
# al - алфавит
# sl - шифруемое слово
# r - регистр шифруемого слова
# sh - шифр
# za - зашифрованное слово
# dl - длина шифруемого слова
al_en = ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
      'p','q','r','s','t','u','v','w','x','y','z']
al = ['я','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о',
      'п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
za = []
sl = list(input('Введите шифруемое слово: '))
sh = list(input('Введите шифр: ').lower())
dl = len(sl)
r = [0]*dl

#продление шифра
if len(sh) < dl:
    for i in range(dl-len(sh)):
            sh.append(sh[i])
#регистр вводимого
for i in range(dl):
    if sl[i].isupper():
        r[i] = 1
        sl[i] = sl[i].lower()

for i in range(dl):
    if not sl[i] in al:
        sh.insert(i, 0)

#шифрование
for i in range(dl):
    if sl[i] in al:
        a = ((al.index(sl[i]) + al.index(sh[i]))%33) - 1
        za.append(al[a])
    else:
        za.append(sl[i])
#возврат регистра
for i in range(dl):
    if r[i] == 1:
        za[i] = za[i].upper()
#вывод
for i in za:
    print(i,end='')