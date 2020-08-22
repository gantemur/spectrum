import math

def rbk(n,k):
    b = math.sqrt(((k+1)*(k+1) - n*n)/(k*(k+2)))
    alpha = math.asin(b)
    beta = math.asin(b/n)
    delta = (k+1)*math.pi +2*alpha - 2*(k+1)*beta
    delta = delta%(2*math.pi)
    if delta > math.pi : delta = 2*math.pi-delta
    if delta > math.pi/2 : delta = delta - math.pi
    return [alpha,beta,delta]
    
def rbkdeg(n,k):
    a = rbk(n,k)
    return [a[0]*180/math.pi,a[1]*180/math.pi,a[2]*180/math.pi]
    
    
n1 = 1
n2 = 1.333333
n = n2/n1

for k in range(1,6):
    a = rbkdeg(n,k)
    print(k,'%0.2f'%a[0],'%0.2f'%a[1],'%0.2f'%a[2])
