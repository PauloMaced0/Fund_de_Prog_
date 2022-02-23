seg = int(input('Tempo em segundos?'))

h = seg//3600
resto = seg%3600
m = resto//60
s = resto%60

print('{:02d}:{:02d}:{:02d}'.format(h,m,s))