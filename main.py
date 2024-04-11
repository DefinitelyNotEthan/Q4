import math
def mass():
  P = int(input("What is the orbital period of a body orbiting this star?: "))
  a = int(input("How far is the body from that star?: "))
  p2 = P * P
  a3 = a * a * a
  M = p2 / a3
  print("The star has a mass of " + str(m) + "M☉!")
def distance():
  M = int(input("What is the mass of your star (in solar mass)?: "))
  P = int(input('What is the orbital period of your body (in earth years)?: '))
  p2 = P * P
  a3 = M * p2
  a = a3**(1/3)
  print("The body is " + str(a) + "AU from its star!")
def period():
  a = int(input("What the distance of your body from its star in AU? "))
  M = int(input("What is the mass of your star (in solar mass)?: "))
  a3 = a**3
  p2 = a3/M
  p = p**(1/2)
  print('It takes your body ' + str(p) + ' Earth years to complete an orbit!')
def choice():
  userChoice = input("What do you want to calculate (type: mass, distance, or orbital period)? ")
  if userChoice == 'mass':
    mass()
  elif userChoice == 'distance':
    distance()
  elif userChoice == 'orbital period':
    period()
  else:
    print('''
    please type mass, distance, or orbital period! ''')
    choice()
