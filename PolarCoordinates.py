# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
comp = complex(input(""))
print(abs(complex(comp.real, comp.imag)))
print(cmath.phase(complex(comp.real, comp.imag)))