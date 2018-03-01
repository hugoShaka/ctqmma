# -*- coding: utf-8 -*-


#Imports librairies
import sys

#Import classes et methodes

import trajets
import car

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




def temps_min_course(car,rides,T):
    min_tmps=T
    id=0
    for i in range(len(rides)-1):
        #si le trajet n'est pas pris
        if rides[i].estReserve==False and min_tmps > rides[i].s :
            #verifier si faisable
            if rides[i].estFaisable(car.x,car.y,car.tps):
                min_tmps=rides[i].s
                id = rides[i].ident

    return min_tmps,id


def affecter_trajet(car,rides,B,T):

    #affecter à la voiture le temps de trajet min des trajets non affectés
    min_tmps,id_ride = temps_min_course(car,rides,T)
    if min_tmps>car.tps :
        car.tps = min_tmps


    rides[id_ride].estReserve=True #trajet fait
    car.trajets.append(rides[id_ride])#ajout trajet aux trajets de la voiture
    car.x = rides[id_ride].x
    car.y = rides[id_ride].y

    rides[id_ride].printTraj()

    car.printCar()


def affecter_tous_trajets(cars,rides,B,T):
    nb_fini=0
    while nb_fini < len(cars)-1:
        nb_fini = 0
        for i in range(len(cars)-1):
            if cars[i].tps<T:
                affecter_trajet(cars[i],rides,B,T)
            else :
                nb_fini +=1
        print("ICI §§§§§§§§§§§§§",nb_fini)




def export(fichier, cars):
  """Parse le fichier"""
  data=open(fichier + "_res" ,"w")
  for car in cars:
      trajets = ""
      for i in range(len(car.trajets)-1):
          trajets = trajets + ' ' + str(car.trajets[i].ident)
      car_result = str(len(car.trajets)-1) + " " + trajets
      data.write(car_result + "\n")


def main():
    file = "C:/Users/Juliette/Documents/hashcode/e_high_bonus.in"
    #file = sys.argv[1]
    print ("opening file"+ " "+ file)

    (R, C, F, N, B, T, rides, cars) = parse(file)


    # Have fun :)


    affecter_tous_trajets(cars,rides,int(B),int(T))
    export(file,cars)






if __name__ == '__main__':
    main()
