print('''
                       :
                       :
                       :
                       :
        .              :
         '.            :           .'
           '.          :         .'
             '.   .-""""""-.   .'                                   .'':
               '."          ".'                               .-""""-.'         .---.          .----.        .-"""-.
                :            :                _    _        ."     .' ".    ..."     "...    ."      ".    ."       ".
        .........            .........    o  (_)  (_)  ()   :    .'    :   '..:.......:..'   :        :    :         :   o
                :            :                              :  .'      :       '.....'       '.      .'    '.       .'
                 :          :                             .'.'.      .'                        `''''`        `'''''`
                  '........'                              ''   ``````
                 .'    :   '.
               .'      :     '.
             .'        :       '.
           .'          :         '.
                       :
                       :
                       :
                       :
                       ''')
print(''' 
__        __   _                                 
\ \      / /__| | ___ ___  _ __ ___   ___        
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \       
  \ V  V /  __/ | (_| (_) | | | | | |  __/       
 _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|       
| |_ ___   |_   _| |__   ___                     
| __/ _ \    | | | '_ \ / _ \                    
| || (_) |   | | | | | |  __/                    
 \__\___/    |_|_|_| |_|\___|                    
| |/ /___ _ __ | | ___ _ __                      
| ' // _ \ '_ \| |/ _ \ '__|                     
| . \  __/ |_) | |  __/ |                        
|_|\_\___| .__/|_|\___|_|_       _             _ 
 / ___|__|_| | ___ _   _| | __ _| |_ ___  _ __| |
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| |
| |__| (_| | | (__| |_| | | (_| | || (_) | |  |_|
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  (_)

''')
def mass():
  P = float(input("What is the orbital period of a body orbiting this star(in Earth Years)?: "))
  a = float(input("How far is the body from that star (in AU)?: "))
  p2 = P * P
  a3 = a * a * a
  M = p2 / a3
  em = M*333000
  print("The star has a mass of " + str(M) + "M☉ or " + str(em) + " Earths!")
def distance():
  M = float(input("What is the mass of your star (in solar mass)?: "))
  P = float(input('What is the orbital period of your planetary body (in earth years)?: '))
  p2 = P * P
  a3 = M * p2
  a = a3**(1/3)
  km = a * (1.496 * 10**8)
  print("The planetary body is " + str(a) + "AU (" + str(km) + " km " + " from its star!")
def period():
  a = float(input("What the distance of your planetary body from its star in AU? "))
  M = float(input("What is the mass of your star (in solar mass)?: "))
  a3 = a**3
  p2 = a3/M
  p = p2**(1/2)
  print('It takes your planetary body ' + str(p) + ' Earth years to complete an orbit!')
def distance2():
  P = float(input("What is the orbital period of the orbiting body (in years)? "))
  m1 = float(input("What is the mass of the object being orbited (in solar mass)? "))
  m2 = float(input("What is the mass of the object orbiting (in solar mass)? "))
  m = (m1 + m2)
  p2 = P**2
  a3 = m * p2
  a = a3**(1/3)
  km = 1.496 * 10**8
  akm = a * km
  print("The orbiting body is " + str(a) + " AU (" + str(akm) + " km) from its host!")
def period2():
  a = float(input("How far apart are these two bodies (in AU)? "))
  m1 = float(input("What is the mass of the object being orbited (in solar mass)? "))
  m2 = float(input("What is the mass of the object orbiting (in solar mass)? "))
  m =(m1 + m2)
  p2 = (a**3)/m
  P = p2**(1/2)
  print("It takes the orbiting body " + str(P) + " years to complete an orbit!")
def choice():
  form = input("Is/are your planetary body(ies) orbiting a star (type yes or no)?: ")
  if form.lower() == 'yes':
    userChoice = input("What do you want to calculate (type: mass, distance, or orbital period)? ")
    if userChoice.lower() == 'mass':
      mass()
    elif userChoice.lower() == 'distance':
      distance()
    elif userChoice.lower() == 'orbital period' or userChoice.lower() == 'period':
      period()
    else:
      print('''
      please type mass, distance, or orbital period! 
      ''')
      choice()
  elif form.lower() == 'no':
    userChoice = input("What do you want to calculate (type: distance or orbital period)? ")
    if userChoice.lower() == 'distance':
      distance2()
    elif userChoice.lower() == 'orbital period' or userChoice.lower() == 'period':
      period2()
    else:
      print('''
      please type mass, distance, or orbital period! 
      ''')
      choice()
choice()
