import math

c1 = float(input('Cateto1?'))
c2 = float(input('Cateto2?'))

h = math.sqrt(math.pow(c1,2)+math.pow(c2,2))
cosang = c1/h
angradian = math.cos(cosang)
angdegree = math.degrees(angradian)

print('Medida da hipotenusa : {:5.3f} e o Ângulo entre o lado A e H:{:4.1f}'.format(h,angdegree))