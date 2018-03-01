 #!/usr/bin/python

#Imports librairies
import sys
sys.path.append(r'C:\Users\Iris de Gélis\Desktop\ctqmma')

#Import classes et methodes
#from parser import parse
#import parser
import trajets
import car

#import hugo/mathieu/iris/juliette.py

def parse(fichier):
  """Parse le fichier"""
  data=open(fichier,"r")

  header=data.readline()
  (R, C, F, N, B, T)=header.split(" ")
  rides =[]
  #Liste des latences
  for i in range(int(N)):
    (a, b, x, y, s, f)=data.readline().split(" ")
    rides.append(trajets.Trajet(i, int(a), int(b), int(x), int(y), int(s), int(f)))

  cars=[]
  for i in range(int(F)):
    cars.append(car.Car(i))

  return(R, C, F, N, B, T, rides, cars)
  
  
#class Car(object):
#    def __init__(self,_id):
#        """
#        Constructeur de la classe Car
#        position
#        tps
#        """
#        self.x = 0
#        self.y = 0
#        self.tps = 0
#        self.id = _id
#        self.trajets = []
#        
#        
#    def printCar(self):
#        print("id = %d, pos = (%d,%d) , tps = %r, trajets = %s" % (self.id, self.x, self.y, self.tps, str(self.trajets)))
#    
#    def maj(new_pos):
#        self.pos = new_pos
#        self.tps +=1
#        
#    def maj2(new_pos,tps):
#        self.pos = new_pos
#        self.tps +=tps
#    
#    def new_trajet(trajet):
#        self.trajets.append(trajet)
        
    
#exampleTraj()
        
#exampleTraj()
def find_nearestCar(traj,cars):
    dist = 1000000000000000
    carChosen = 0
    for ca in cars:
        dist_ca = traj.getStartDistFrom(ca.x,ca.y)
        if dist_ca<dist:
            dist = dist_ca
            carChosen = ca
    return carChosen

def easyWay(R, C, F, N, B, T, rides, cars):
    tps = 0
    for traj in rides:
        carChosen = find_nearestCar(traj,cars)
        carChosen.new_trajet(traj)
        carChosen.maj2=(traj.)
        carChosen.printCar()            
if __name__=="__main__":
    file = "b_should_be_easy.in"
    print("opening file" + file)
    
    (R, C, F, N, B, T, rides, cars) = parse(file)
    
    easyWay(R, C, F, N, B, T, rides, cars)
    
