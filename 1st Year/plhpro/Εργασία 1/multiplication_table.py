def main():
    # Δήλωση μεταβλητής εξόδου, ώστε παρακάτω να είναι σαφές τι αναπαριστά το 0
    EXIT_CONDITION = 0

    """
    Ανάθεση τιμής σε μεταβλητή με την χρήση συνάρτησης. Η χρήση συνάρτησης έγινε, 
    μεταξύ άλλων, για να αποφευχθεί η επανάληψη κώδικα, όπως θα φανεί παρακάτω
    """
    num = get_integer_from_user(1, 10, EXIT_CONDITION)

    # Το πρόγραμμα θα επαναλαμβάνεται μέχρι ο χρήστης να εισάγει το exit condition
    while num != EXIT_CONDITION:

        """
        for loop με ορίσματα το 1 και το 11. Ο λόγος για το 11, αντί του 10, είναι πως η δεύτερη τιμή 
        δεν συμπεριλαμβάνεται στο for loop, άρα εδώ οι επαναλήψεις γίνονται από το 1 στο 10
        """
        for i in range(1, 11):
            print(f"{i} x {num} = {i * num}")

        # Ανάθεση νέας τιμής
        num = get_integer_from_user(1, 10, EXIT_CONDITION)

    # Εκτύπωση "Τέλος προγράμματος"
    print("Τέλος Προγράμματος")

def get_integer_from_user(start, end, exit_condition):
    """
    Το while loop θα "τρέχει", έως ότου οι επαναλήψεις σταματήσουν με την χρήση κάποιου
    control flow statement
    """
    while True:
        """
        Λαμβάνω το input από τον χρήστη και το μετατρέπω σε int απευθείας, καθώς έχω βεβαιωθεί
        από την εκφώνηση πως δεν υπάρχει περίπτωση να λάβω στοιχείο εκτός ακεραίου
        """
        result = int(input(f"Δώστε έναν αριθμό από {start} εώς {end}, ή {exit_condition} για έξοδο: "))

        # Αν λάβω το exit_condition από τον χρήστη, βγαίνω από την while
        if result == exit_condition:
            break

        # Αν ο ακέραιος που θα λάβω έχει αποδεκτή τιμή, βγαίνω από την while
        if start <= result <= end:
            break

    # Επιστρέφω την τιμή που έλαβα από τον χρήστη
    return result

main()