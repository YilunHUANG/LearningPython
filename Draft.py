x = 100
divisers = ()
for i in range(1,x+1):
    if x%i ==0:
        divisers += (i,)
print(divisers)
