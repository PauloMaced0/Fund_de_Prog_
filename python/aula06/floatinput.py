import math

def floatInput(prompt, min=-math.inf, max=math.inf):
    assert min<max
    res = None
    while not res:
        try:
            res = float(input(prompt))
            checkInterval(res, min, max)
        except ValueError as e:
            print("ERROR: Not a float!", e)
            res = None
        except Exception as e:
            print(e)
            res = None
    
    return res

def checkInterval(val, min, max):
    if val < min or val > max:
        raise Exception(f"ERROR: Value {val} does not belong to interval[{min}, {max}]")

def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    assert 0 <= h <= 100,'Must be between [0,100]!'
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", min=-273.15)
    print("t:", t)

    return

if __name__ == "__main__":
    main()