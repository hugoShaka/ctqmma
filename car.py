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
        
        
    def printCar(self):
        print("id = %d, pos = (%d,%d) , tps = %r, trajets = %s" % (self.id, self.x, self.y, self.tps, str(self.trajets)))
    
    def maj(new_pos):
        self.pos = new_pos
        self.tps +=1
    
    def new_trajet(trajet):
        self.trajets.append(trajet)