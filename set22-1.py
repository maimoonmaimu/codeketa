def rpower(n,i):
    if(i==1):
       return(n)
    else:
       return(n*rpower(n,i-1))
base=int(input(" "))
exp=int(input(" "))
rpow=rpower(base,exp)
print("{} raised to {}: {}".format(base,exp,rpow))
