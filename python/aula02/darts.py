import math

x =float(input('x(mm)?'))
y =float(input('y(mm)?'))

r =math.sqrt(math.pow(x,2)+math.pow(y,2))

razao = x/r
ang = math.sin(razao)

if ang<math.pi/20 and ang>0:
    numero=6
elif ang<3*math.pi/20 and ang>math.pi/20:
    numero=13
elif ang<5*math.pi/20 and ang>3*math.pi/20:
    numero=4
elif ang<7*math.pi/20 and ang>5*math.pi/20:
    numero=18
elif ang<9*math.pi/20 and ang>7*math.pi/20:
    numero=1
elif ang<11*math.pi/20 and ang>9*math.pi/20:
    numero=20
elif ang<13*math.pi/20 and ang>11*math.pi/20:
    numero=5
elif ang<15*math.pi/20 and ang>13*math.pi/20:
    numero=12
elif ang<17*math.pi/20 and ang>15*math.pi/20:
    numero=9
elif ang<19*math.pi/20 and ang>17*math.pi/20:
    numero=14
elif ang<21*math.pi/20 and ang>19*math.pi/20:
    numero=11
elif ang<23*math.pi/20 and ang>21*math.pi/20:
    numero=8
elif ang<25*math.pi/20 and ang>23*math.pi/20:
    numero=16
elif ang<27*math.pi/20 and ang>25*math.pi/20:
    numero=7
elif ang<29*math.pi/20 and ang>27*math.pi/20:
    numero=19
elif ang<31*math.pi/20 and ang>29*math.pi/20:
    numero=3
elif ang<33*math.pi/20 and ang>31*math.pi/20:
    numero=17
elif ang<35*math.pi/20 and ang>33*math.pi/20:
    numero=2
elif ang<37*math.pi/20 and ang>35*math.pi/20:
    numero=15
elif ang<39*math.pi/20 and ang>37*math.pi/20:
    numero=10
elif ang>39*math.pi/20 and ang<2*math.pi:
    numero=6
    
if r<6.35:
    pontos = 50
elif r<16 and r>6.35:
    pontos = 25
elif r>170:
    pontos = 0
elif r<106.685 and r>16:
    pontos = numero
elif r>106.685 and r<107:
    pontos = 3*numero
elif r>107 and r<169.685:
    pontos = numero
elif r>169.685 and r<170:
    pontos = 2*numero


print('Pontuação: {} pontos'.format(pontos))



 