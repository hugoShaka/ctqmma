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
        self.active = True
        
        
    def printCar(self):
        print("id = %d, pos = (%d,%d) , tps = %r, trajets = %s" % (self.id, self.x, self.y, self.tps, str(self.trajets)))
    
    def maj(self, new_pos):
        self.pos = new_pos
        self.tps +=1

    def maj2(self, new_pos, new_time):
        self.pos = new_pos
        self.tps = new_time
    
    def new_trajet(self, trajet):
        self.trajets.append(trajet)
    def disactive(self):
        self.active = False