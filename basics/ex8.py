import random 


n = random.randint(1,10) 

print("Estoy pensando un numero entre 1 y 10, adivinalo!!") 

running = True 
while running: 
    guess_str = input("Tu piensas que es el numero:  ") 
    guess = int(guess_str) 
    if guess == n: 
        print("Muy bien, " + str(guess) + " es correcto!") 
        running = False 
    elif guess < n: 
        print("Intenta con un numero mayor") 
    else: 
        print("Intenta con un numero menor")
        
