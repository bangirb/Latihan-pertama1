import math

# Input diameter dan tinggi kerucut
diameter = 5
tinggi = 4

# Hitung jari-jari dari diameter
jari_jari = diameter / 2

# Hitung volume kerucut dengan rumus: (1/3) * pi * r^2 * tinggi
volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi

# Output hasil volume kerucut
print(f'Volume kerucut dengan diameter {diameter} dan tinggi {tinggi} adalah {volume:.2f}')
