a = 1
b = 2
c = 3

d = (c > b) and (a > b)
e = c > (b == a)
f = c != ((a == b) and (b != a))

print("Resultados: ")
print(f"({c} > {b}) and ({a} > {b}) isso é {d}")
print(f"{c} > ({b} == {a}) isso é {e}")
print(f"{c} != (({a} == {b}) and ({b} != {a})) isso é {f}")