def hms2sec(h, m, s):   
   sec = h*3600 + m*60 + s
   return sec
def main():
   hora = int(input('h?'))
   minuto=int(input('m?'))
   segundo=int(input('s?'))
   
   seg=hms2sec(hora, minuto, segundo)
   print(seg,'segundos')

main()