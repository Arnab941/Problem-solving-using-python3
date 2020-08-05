speed=float(input())
lati=float(input())
hr=(((speed/360)*lati)%12)*60
mini=hr%60
taxi=abs((hr/2)-(mini*6))
print('{:.2f}'.format(taxi))