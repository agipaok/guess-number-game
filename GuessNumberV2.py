# ΠΡΟΓΡΑΜΜΑ ΜΑΝΤΕΨΙΑΣ ΑΡΙΘΜΟΥ
import random

#ΜΕΤΑΒΛΗΤΕΣ ΓΙΑ ΠΡΟΣΠΑΘΕΙΕΣ , ΠΑΙΧΝΙΔΙΑ ΚΑΙ ΑΛΛΑ

games_played = 0
user_win = 0
pc_win = 0

# ΑΡΧΗ ΠΡΟΓΡΑΜΜΑΤΟΣ
print("Καλωσήρθατε στο πρόγραμμα που πρέπει να μαντέψετε τον αριθμό μέσα σε 5 προσπάθειες")
print("Θα ξεκινησουμε διαλέγοντας ένα αριθμό")
user_name = input("Πως να σε αποκαλώ?: ")

while True:
    tries = 0
    #ΕΛΕΓΧΟΥΜΕ ΑΝ Ο ΧΡΗΣΤΗΣ ΔΩΣΕΙ ΣΩΣΤΟ ΑΡΙΘΜΟ ΩΣΤΕ ΝΑ ΜΗΝ ΠΕΤΑΞΕΙ ERROR
    while True:
        try:
            user_input = int(input("Δώσε ένα αριθμό από το 0 έως το 20: "))
            if user_input >= 0 and user_input <= 20:
                break
            else:
                print("Δώσε σωστό αριθμό! (0-20)")
        except ValueError:
            print("Παρακαλώ μόνο νούμερα!!")

    #ΕΔΩ ΔΗΜΙΟΥΡΓΟΥΜΕ ΤΟΝ ΑΡΙΘΜΟ
    number = random.randrange(0,20)
    print(number)

    #ΚΑΙ ΕΔΩ ΕΛΕΓΧΟΥΜΕ ΑΝ Ο ΧΡΗΣΤΗΣ ΔΩΣΕΙ ΣΩΣΤΟ ΑΡΙΘΜΟ ΩΣΤΕ ΝΑ ΜΗΝ ΠΕΤΑΞΕΙ ERROR ΚΑΙ ΣΥΓΚΡΙΝΟΥΜΕ ΤΟΥΣ ΑΡΙΘΜΟΥΣ
    while tries < 4:
            
        if user_input > number:
            try:
                user_input = int(input("Είναι μικρότερος!  Προσπάθησε ξανά: "))
                tries += 1
            except ValueError:
                print("Παρακαλώ μόνο νούμερα!!")
        elif user_input < number:
            try:
                user_input = int(input("Είναι μεγαλύτερος! Προσπάθησε ξανά: "))
                tries += 1
            except ValueError:
                print("Παρακαλώ μόνο νούμερα!!")
        else:
            print(f"\nBingo!! Τον βρήκες με την {tries+1}η φορά!")
            user_win += 1
            games_played += 1
            print(f"\nΤο σκόρ μεταξύ υπολογιστή και του {user_name} είναι: {pc_win} - {user_win}")
            break
        
        
    if tries == 4:
        print(f"\nLooser!!! ο αριθμός ήταν {number}")
        pc_win +=1
        games_played += 1
        print(f"\nΤο σκόρ μεταξύ υπολογιστή και του {user_name} είναι: {pc_win} - {user_win}")
        
    # ΕΔΩ ΕΛΕΓΧΟΥΜΕ ΑΝ ΘΕΛΕΙ ΝΑ ΠΑΙΞΕΙ ΚΑΙ ΑΛΛΟ
    print("\nΘέλεις να ξαναδοκιμάσεις? (ΝΑΙ/ΟΧΙ)")
    user_answer = input(">")
    if user_answer.lower().strip() != "ναι":
        break
    else:
        continue 

print("END OF GAME")
    
