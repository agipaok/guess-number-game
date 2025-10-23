import random

print("Καλωσήρθατε στο πρόγραμμα που πρέπει να μαντέψετε τον αριθμό μέσα σε 5 προσπάθειες")
print("Θα ξεκινησουμε διαλέγοντας ένα αριθμό")

while True:
    user_input = int(input("Δώσε ένα αριθμό από το 0 έως το 20: "))
    if user_input >= 0 and user_input <= 20:
        break
    else:
        print("Δώσε σωστό αριθμό! (0-20)")

number = random.randrange(0,20)

tries = 0
    
while tries != 5:
    tries += 1
    if user_input > number:
        user_input = int(input("Είναι μικρότερος!"))
    elif user_input < number:
        user_input = int(input("Είναι μεγαλύτερος!"))
    else:
        print(f"Bingo!! Τον βρήκες με την {tries}η φορά!")
        break

if tries == 5:
    print(f"Looser!!! ο αριθμός ήταν {number}")