# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_template= 'Hello, person!'):
               
    if greeting_template != 'Hello, person!':
        
        greeting = str('What\'s up, '+ name+'!' )
        #print(greeting)
        return greeting
        
    else:
        
        greeting = greeting_template.replace('person', name)
        #print(greeting)
        return greeting

greet('Doc')
greet('Bob', "What's up, <name>!")

def force(mass, body= 'earth'):
    body_list = {
        'sun': 274,
        'jupiter':24.92,
        'neptune':11.15,
        'saturn':10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto':0.59,
        }
    body_calc = round(body_list[body],1)
    #print(body_calc)
    force=round(mass*body_calc,2)
    #print(force)
    
    return force

force(0.1, 'venus')

def pull(m1, m2, d):
    G=6.674 * (10 ** -11)
    #force=("{:.6f}".format(G * ((m1 * m2) / d ** 2)))
    force = round(float(((G * (((m1 * m2) / d ** 2))))))
   
    #print(force)
    return force
    

pull(800,1500,3)



