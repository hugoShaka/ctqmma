#!/usr/bin/python

#Imports librairies
import sys

#Import classes et methodes
from parser import parse
from exporter import export
import trajets
import car

#import hugo/mathieu/iris/juliette.py

file = sys.argv[1]

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

def got_bonus(ride, car):
    return ride.s - ride.getStartDistFrom(car.x, car.y) == car.tps

def ratio(car, ride):
    distance_totale = ride.getTimeToEnd(car.x, car.y, car.tps)
    if got_bonus(ride, car):
        bonus = int(B)
    else:
        bonus = 0
    point = float(bonus + ride.distance)
    ratio = point/distance_totale
    return(ratio)

def meilleur_trajet_score(car, rides):
    best_ratio = 0
    best_trajet = None
    for ride in rides:
        if ratio(car,ride) > best_ratio and ride.estFaisable(car.x, car.y, car.tps) and not ride.estReserve:
            best_dist = ride.getStartDistFrom(car.x, car.y)
            best_trajet = ride

    return(best_trajet)


for car in cars:
    count = 0
    cont = True
    while cont == True:
        count += 1
        print(count)
        trajet = meilleur_trajet_score(car, rides)
        if trajet == None:
            cont = False
        else:
            rides[trajet.ident].estReserve = True
            car.maj2((trajet.x, trajet.y), trajet.getTimeToEnd(car.x, car.y, car.tps))
            car.new_trajet(trajet.ident)
    
    print(car.trajets)

export(file, cars)

