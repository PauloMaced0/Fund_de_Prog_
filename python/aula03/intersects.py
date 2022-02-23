def intersects(x,y,z,k):
    assert x<=y and z<=k
    if y<z:
        return False
    else:
        return True
def main():
    a1 =float(input('?')) 
    a2 =float(input('?'))
    b1 =float(input('?'))
    b2 =float(input('?'))

    valor=intersects(a1,a2,b1,b2)
    print('',valor)
main()