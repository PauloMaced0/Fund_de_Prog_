d1 =float(input('Distância (km)')) 
t1 =float(input('Tempo ida?(h)'))
t2 =float(input('Tempo volta?(h)'))

vmi = d1/t1
vmv = d1/t2
vmdaviagem = (vmi+vmv)/2

print('Velocidade média da viagem : {} (km/h)'.format(vmdaviagem))
