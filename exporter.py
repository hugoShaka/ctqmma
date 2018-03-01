import trajets
import car

def export(fichier, cars):
  """Parse le fichier"""
  data=open(fichier + ".res" ,"w")
  for car in cars:
      trajets = ""
      for i in range(len(car.trajets)):
          trajets = trajets + ' ' + str(car.trajets[i])
      car_result = str(len(car.trajets)) + " " + trajets
      data.write(car_result + "\n")

