# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#############################PART1#################################
def greet(name,greeting="Hello"):
    greeting = (f"{greeting} {name}")
    return greeting
    
print(greet("Bob"))

#############################PART2#################################
def force(mass, body= "earth"):
    body.lower()
    gravity_object = dict(mercury= 3.7, venus=8.9, earth=9.8, moon= 1.6, mars = 3.7, jupiter= 23.1, 
                      saturn = 9.0, uranus = 8.7, neptune = 11.0, pluto = 0.7)
    force = round(mass*gravity_object[body],1)
    force_string = (f"The force of {body} is {force}")
    return force_string

print(force(0.33,"mercury"))

##########################PART3####################################

def pull(m1,m2,d):
    g = 6.673*(10**(-11))
    pull = g *(m1*m2)/d**2
    return pull
    
m1 = float(input())
m2 = float(input())
d =  float(input())

print(pull(m1,m2,d))

########################PART4######################################

