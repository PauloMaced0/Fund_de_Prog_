def mdc(a,b):
    r=a%b
    if r==0:
        return b
    if r>0:
        return mdc(b,r)
def main():
    value1=int(input('valor?'))
    value2=int(input('valor?'))

    mdcom=mdc(value1,value2)
    print(mdcom)

main()