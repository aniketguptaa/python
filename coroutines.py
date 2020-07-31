# We are going to use coroutines bahut vistrit (comprehensive topic hai)
'''Why use coroutines
Featured snippet from the web
Coroutines are useful to get rid of callbacks.
Assume that you have a function that must perform some expensive computation:
solveAllProblems . This function calls a callback that receives the result of the computation and
performs what is needed (e.g., it saves the result in a database).'''

def library_book_finder(): # Creating a function of library book finder (Coroutine)
    import time # Importing time module to use built in sleep function
    book_shelf = ["The Alchemist","The Intelligent Investor","Tesla","The Fault in Our Stars"] # Book Shelf
    time.sleep(2) # Delaying the time because user think his book is searching

    while True:
        find_book = (yield)  # Generating each book in the book shelf
        if find_book in book_shelf:    # Finding is his requested book is available
            print(find_book,"is available") # His requested book is available
        else:
            print(find_book,"is not available")  # His requested book is not available

person_finding_a_book = library_book_finder() # Assigning the person in the library
next(person_finding_a_book)   # Linked him with generators to find next book 
person_finding_a_book.send('The Alchemist') # Sending a query or request

# For example we are prompting user if he had another request
input('Do You Wanna Find More Books?')  # Asking a query just after processing his previous query
person_finding_a_book.send('The Biology Weapons')  # Performed an instance action (Not available)
person_finding_a_book.close() # Closing the search query

# chaliye jaante hai coroutine ke baare me asal zindagi se jorkar
# maan lijiye aap apne school ke library me gaye aur aapne, aur waha ke library
# assistant se aapne kaha ki mujhe "The alchemist" naamak book chahiye, aap use 
# dhoond kar nikaliye, librarian ne bola OK rukiye me book shelf se 'The alchemist'
# naamak book khojta hu, maan lijiye librarian ne aapki kitaab ko 10 minute me khoj kar
# nikaala aur aapko aake usne kaha yeh lo The alchemist naam ka book available hai.
# aapne woh book apne bag me rakh liya aur aapko fir achanak yaad aaya ki aapke bare
# bhai ne bola tha ki 'The intelligent investor' naamak book mere liye library se lete aana
# aapne librarian se kaha ki 'the intelligent investor' naam ka book library me hai kya
# isspar librarian ne aapko turant jawaab diya ki "Intelligent investor naamak book hai"
# aapne usse woh book bhi le liya. yaha dhyaan dene waali baat yeh hai ki jab aapne 
# the alchemist book librarian se maanga tha toh usne 10 minute ka samay liya tha, usne
# aapki kitaab ko khoja usme usko samay laga lekin aapke bhai ke kitaab ko usne turant 
# de diya qki jab woh aapki kitaab ko khoj raha tha woh saare kitaabon ko dekhta jaa raha 
# tha toh usne 'the intelligent investor' waala kitaab bhi dekh liya tha, toh usko pata
# chal gaya tha ki yeh kitaab yaha rakhi huyi hai, toh aapke maangne par use pata tha
# ki yeh kitaab yaha hai usne turant woh kitaab aapko de diya. aur iss baar aapka samay bhi
# na ke barabar laga.

# yahi logic python me coroutine ke saath hai yaha aapne usse kaha mujhe yeh book chahiye 
# usne aapne book ko khojne me 2 second lagaya lekin jab aapne bola mujhe yeh bhi kitaab chahiye
# toh usne turant bataya ki yeh kitaab hai ya nahi hai.

# yaha par hamlogo ne pehle ek function define kiya hua hai











