
def fun(x):
 return X
def bisection( x,x1,e):
 x0 = float(input('lower limit:'))
 x1 = float(input('upper limit:'))
 error = float(input('tolerance:'))
step = 1
condition = True
while condition:
 x2= (x0 +x1)/2
print('Iteration-d,x2= 0.6f and f(x2) =0.6f' %(step,x2,f(x2)) )
if f(x)* f(x2) < 0:
 x1= x2
else:
 x0= x2

step= step +1
condition = abs( f(x2))> e
print('/n  root is : %0.8f' % x2)
if f(x0)*f(x1)>0:
 print('try again')
else:
 bisection(x0,x1,e)