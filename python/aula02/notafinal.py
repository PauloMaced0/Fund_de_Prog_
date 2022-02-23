atp = float(input('Nota TP?'))
ap = float(input('Nota P?'))

nota = 0.36*atp + 0.64*ap

if atp<6.5 or ap<6.5:
    print('Reprovado!') 
    exit(1) # termina a execução do programa!
elif nota < 9.5:
    print('!RECURSO!')
    notarecursotp = float(input('Nota recurso TP?'))
    notarecursop = float(input('Nota recurso P?'))
    nfr = 0.36*notarecursotp + 0.64*notarecursop
    print('Nota final: {:2.0f}',nfr)
else:
    print('Nota final:{:2.0f}'.format(nota))
