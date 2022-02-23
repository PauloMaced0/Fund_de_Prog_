def sec2hms(sec):
    h = sec//3600
    print(h)
    resto=sec%3600
    print(resto)
    m= resto//60
    print(m)
    s = resto%60
    print(s)
    return h,m,s
def main():
    seg=int(input('segundos?'))

    segu=sec2hms(seg)
    print(segu,'(hora,minuto,segundo)')

main()
