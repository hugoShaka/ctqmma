class Car(object):
    def __init__(self,_id):
        """
        Constructeur de la classe Car
        position
        tps
        """
        self.x = 0
        self.y = 0
        self.tps = 0
        self.id = _id
        self.trajets = []
        self.isBusy = False
        
        
    def printCar(self):
        print("id = %d, pos = (%d,%d) , tps = %r, trajets = %s" % (self.id, self.x, self.y, self.tps, str(self.trajets)))
    
    def maj(self,x,y):
        self.x = x
        self.y = y
        self.tps +=1
    
    def new_trajet(self,trajet):
        self.trajets.append(trajet)

    def maj2(self,x,y,tps):
        self.x = x
        self.y = y
        self.tps += tps