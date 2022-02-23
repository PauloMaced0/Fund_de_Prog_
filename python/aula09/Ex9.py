import math

def integrate(f, a, b, n):
   """The integral of f(x) for x between a and b.
   Aproximated using the trapezoidal rule with n uniform subintervals."""
   assert n >= 1
   area = 0
   i = b-a
   d = (i)/n
   while a < b:
      k = a+d
      if f(a)<f(k):
         triangle = ( d * (f(k)-f(a))  / 2)
         area += ( d * f(a) ) + triangle
      else:
         triangle = ( d * (f(a)-f(k))  / 2)
         area += ( d * f(k) ) + triangle
      a += d
   return area
 
def example(n):
   f = lambda x: (x-2)/(x+3)
   a = integrate(f, 0, 1, n)
   return a
