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
  
        
#exampleTraj()
def find_nearestCar(traj,cars,B):
    dist = 1000000000000000
    cpt = 0
    for ca in cars:
        tReachStart,tWait,tBonus,tTotal,tReachEnd = traj.getCostFrom(ca.x,ca.y, ca.tps,B)
        if ca.tps+tTotal <traj.f:
            dist_ca = traj.getStartDistFrom(ca.x,ca.y)
            print(dist_ca)
            if dist_ca<dist:
                dist = dist_ca
                carChosen = cpt
        cpt +=1
        print(carChosen)
    return carChosen, tTotal

def easyWay(R, C, F, N, B, T, rides, cars):
    tps = 0
    for traj in rides:
        car,tTotal = find_nearestCar(traj,cars,B)
        print("ok")
        cars[car].id
        cars[car].new_trajet(traj)
        cars[car].maj2=(traj.x,traj.y,tTotal)
        #cars[car].printCar() 
if __name__=="__main__":
    #file = "b_should_be_easy.in"
    file = "a_example.in"
    print("opening file" + file)
    
    (R, C, F, N, B, T, rides, cars) = parse(file)
    
    easyWay(int(R), int(C), int(F), int(N), int(B), int(T), rides, cars)
    
