
from decimal import Decimal

kind = "nothing"
print('''
__        __   _                            _        
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
 _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
| |_| |__   ___  |  _ \| | __ _ _ __ | | __          
| __| '_ \ / _ \ | |_) | |/ _` | '_ \| |/ /          
| |_| | | |  __/ |  __/| | (_| | | | |   <           
 \__|_| |_|\___| |_|   |_|\__,_|_| |_|_|\_\          
|  _ \ ___| | __ _| |_(_) ___  _ __                  
| |_) / _ \ |/ _` | __| |/ _ \| '_ \                 
|  _ <  __/ | (_| | |_| | (_) | | | |                
|_|_\_\___|_|\__,_|\__|_|\___/|_|_|_|          _     
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __| |    
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__| |    
| |__| (_| | | (__| |_| | | (_| | || (_) | |  |_|    
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  (_)    
''')
def scieNo(f):
    return '%.2E' % Decimal(f)

def energy():
    f = float(input("What is the frequency of your photons (in Hz)? "))
    h = 6.626 * (10**-34)
    e = h * f 
    print("Your photons have " + str(e) + " J of energy!")
def freq():
    e = float(input("What is the energy (in J) of your photons? "))
    h = 6.626 * (10**-34)
    f = e/h
    if f < 3*(10**9):
        kind = "radio" 
    elif f > 3 * (10**9) and f < 3 * (10**12):
        kind = "microwaves"
    elif f > 3 * (10**12) and f < 4.3 * (10**14):
        kind = "infrared"
    elif f > 4.3 * (10**14) and f < 7.5 * (10**14):
        kind = "visible light"
    elif f > 7.5 * (10**14) and f < 3 * (10**17):
        kind = "ultraviolet"
    elif f > 3 * (10**17) and f < 3 * (10**19):
        kind = "X-Rays"
    else:
        kind = "Gamma Rays"
    if kind != "microwaves" or kind != "visible light" or kind != "X-Rays" or kind != "Gamma Rays":
        print("Your photons have a frequency of " + str(f) + " Hz! They are " + kind + " waves!")
    elif kind == "microwaves":
        print("Your photons have a frequency of " + str(f) + " Hz! They are " + kind + "!")
    elif kind == "visible light":
        print("Your photons have a frequency of " + str(f) + " Hz! They are " + kind + "!")
    elif kind == "X-Rays":
        print("Your photons have a frequency of " + str(f) + " Hz! They are " + kind + "!")
    else:
        print("Your photons have a frequency of " + str(f) + " Hz! They are " + kind + "!")
def uchoice():
    userC = input('''What would you like to calculate (type "energy" or "frequency")? ''')
    if userC.lower() =="energy":
        energy()
    elif userC.lower() == "frequency":
        freq()
    else:
        print('''
              Please type either "energy" or "frequency"! ''')
        uchoice()
uchoice()
