#!/usr/bin/python

#Imports librairies
import sys

#Import classes et methodes
#from parser import parse
from exporter import export
import trajets
import car

def parse(fichier):
  """Parse le fichier"""
  data=open(fichier,"r")
  print("openned")
  header=data.readline()
  print("header read")

  (R, C, F, N, B, T)=header.split(" ")

  rides =[]
  #Liste des latences
  for i in range(int(N)):
    print("reading line %r" %i)
    (a, b, x, y, s, f)=data.readline().split(" ")
    rides.append(trajets.Trajet(i, int(a), int(b), int(x), int(y), int(s), int(f)))

  cars=[]
  for i in range(int(F)):
    cars.append(car.Car(i))
  print("returning")
  return(R, C, F, N, B, T, rides, cars)
  
#import hugo/mathieu/iris/juliette.py

file = "b_should_be_easy.in"

(R, C, F, N, B, T, rides, cars) = parse(file)

# Have fun :)


#logique une voiture


def meilleur_trajet_naif(car, rides):
    best_dist = 1000000000000000000000
    best_trajet = None
    for ride in rides:
        if ride.getStartDistFrom(car.x, car.y) < best_dist and ride.estFaisable(car.x, car.y, car.tps) and not ride.estReserve:
            best_dist = ride.getStartDistFrom(car.x, car.y)
            best_trajet = ride

    return(best_trajet)

def car_passe(cars):
    tps = 100000000000000
    for car in cars:
        print(car.tps)
        if car.tps<tps:
            ca = car
    return ca
    
for car in cars:
    count = 0
    cont = True
    while cont == True:
        count += 1
        print(count)
        trajet = meilleur_trajet_naif(car, rides)
        if trajet == None:
            cont = False
        else:
            rides[trajet.ident].estReserve = True
            car.maj2((trajet.x, trajet.y), trajet.getTimeToEnd(car.x, car.y, car.tps))
            car.new_trajet(trajet.ident)
    
    print(car.trajets)
ca = car_passe(cars)
export(file, cars)

