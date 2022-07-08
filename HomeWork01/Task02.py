# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def checker(x, y, z):
    return not (x or y or z) == (not x and not y and not z)


a = True
b = False

print(checker(a, a, a))
print(checker(a, a, b))
print(checker(a, b, b))
print(checker(b, b, b))
print(checker(b, b, a))
print(checker(b, a, a))
