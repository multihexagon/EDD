x = 0
y = 0
i = 0


def mcm(x,y,i):
            if(i%x==0 and i%y==0):
                return i
            else:
                return mcm(x,y,i+1)

mcm(10,3,1)
