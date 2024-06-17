import json
fn = input()
# Открываем файл для чтения
with open(fn, 'r') as f:
    # Загружаем данные из файла
    data = json.load(f)
glas = ['a', 'o', 'e', 'u', 'i', 'y']
dic = {}
for x in range(1, len(data)+1):
    s = input().split(sep='_')
    slova = []
    if data[str(x)] == '10':
        for i in s:
            k = 0
            m = []
            for j in i:
                if j in glas and j not in m:
                    m.append(j)
                    k += 1
            if k >= 2:
                slova.append(i)
        slova.sort(reverse=True)
        dic[str(x)] = slova
    elif data[str(x)] == '20':
        for i in s:
            if len(i) % 2 == 0:
                slova.append(i)
        slova.sort(reverse=True)
        dic[str(x)] = slova
    elif data[str(x)] == '30':
        for i in s:
            slova.append(i)
        slova.sort(reverse=True)
        dic[str(x)] = slova
with open('output.json', 'w') as f:
    json.dump(dic, f)

