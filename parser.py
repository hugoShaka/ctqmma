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

