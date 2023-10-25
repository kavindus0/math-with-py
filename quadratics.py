from pylab import *
x = linspace(-10, 10)
coef=[0,1,2]
for i in coef:
  coef[i] = int(input(f"{i+1} coefficient: "))
y = coef[0]*x*x + coef[1]*x + coef[2]
plot(x, y)
show()
