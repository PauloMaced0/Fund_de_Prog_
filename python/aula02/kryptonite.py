print('Kryptonite phase classifier')

t = float(input('Temperature (K)?'))
p = float(input('Pressure (KPa)?'))

if (p/t)<(1/8) and p<50:
    phase = 'gas'
elif (p/t)>(1/8) and t<400:
    phase = 'solid'
elif t>=400 and p>=50:
    phase = 'liquid'
print('At {:3.1f} K and {:3.1f} KPa, Kryponite is in the {} phase. '.format(t,p,phase))

