
class Trajet(object):
    
    def __init__(self,ident,a,b,x,y,s,f):
        self.ident=ident
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        self.s=s
        self.f=f
        self.estReserve=False
        self.distance=abs(a-x)+abs(b-y)
        
    def printTraj(self):
        print("(%d:%d) -> (%d:%d), start = %d, finish = %d, estReserve = %r, distance = %d" % (self.a, self.b, self.x, self.y, self.s, self.f, self.estReserve, self.distance))
        
    def getStartDistFrom(self,ptX,ptY):
        return (abs(self.a-ptX)+abs(self.b-ptY))
    
    def getEndDistFrom(self,ptX,ptY):
        return (abs(self.x-ptX)+abs(self.y-ptY))
    
    # tReachStart : arrivee au point de depart
    # tWait : temps d'attente au depart (peut etre negatif si retard)
    # tBonus : 
    def getCostFrom(self,ptX,ptY,t):
        tReachStart=t+self.getStartDistFrom(ptX,ptY);
        tWait=self.s-tReachStart
        tBonus=self.f-self.distance-tReachStart
        return (tReachStart,tWait,tBonus)
    
    def estFaisable(self,ptX,ptY,t):
        return (self.f-self.distance-self.getStartDistFrom(ptX,ptY) > t)
        
def exampleTraj():
    traj1=Trajet(1,2,3,4,5,2,7);
    traj1.printTraj()
    print (str(traj1.getStartDistFrom(0,0)))
    print (str(traj1.getEndDistFrom(0,0)))
    print (str(traj1.estFaisable(0,0,0)))
    print (str(traj1.estFaisable(2,3,0)))
    print (str(traj1.estFaisable(2,3,2)))
    print (str(traj1.estFaisable(2,3,3)))
    print (str(traj1.estFaisable(2,3,4)))
    print (str(traj1.getCostFrom(2,3,2)))
    print (str(traj1.getCostFrom(2,1,1)))
    print (str(traj1.getCostFrom(2,2,0)))
        
#exampleTraj()