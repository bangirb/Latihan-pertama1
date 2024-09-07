import math

# Input nilai a dan b
a = 3
b = 4

# Hitung KPK menggunakan rumus KPK = (a * b) // FPB
kpk = (a * b) // math.gcd(a, b)

# Output hasil KPK
print(f'KPK dari {a} dan {b} adalah {kpk}')
