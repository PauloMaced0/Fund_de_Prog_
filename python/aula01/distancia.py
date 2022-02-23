import math

xa = float(input('xa?'))
ya = float(input('ya?'))
xb = float(input('xb?'))
yb = float(input('yb?'))

dist = math.sqrt(math.pow((xb-xa),2)+math.pow((yb-ya),2))

print('Distância entre A e B é de {:4.2f}'.format(dist)) 