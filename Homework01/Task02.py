# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат

flag = True
for x in True, False:
    for y in True, False:
        for z in True, False:
            res = not (x or y or z) == (not x and not y and not z)
            print(f'{x} {y} {z} {res}')
            if not res:
                flag = False

if flag:
    print('It\'s correct')
else:
    print('It\'s not correct')
