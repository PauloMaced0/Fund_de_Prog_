def main():
    print("{:3s} {:3s} {:3s}".format("n", "n²", '2**n'))
    x=range(1,21)
    for n in x:
        print("{:3d} {:3d} {:3d}".format(n, n**2, 2**n))   

main()

