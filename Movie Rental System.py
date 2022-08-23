# Nilufer Demirbas

# 05/16/2022

# The following program allows the user to rent movies that are avaliable in the system, return them, see the total price,
# see their purchase history, and check which movies they are currently renting.


from tkinter import *
from tkinter import ttk

# class Movies
class Movies:

    def __init__(self, receipt, purchase_history):
        self.purchase_history = purchase_history
        self.receipt = receipt 

    def receipt(movie_price):
        '''The for loop grabs values from the movie_price list and prints them out
        with the sum of all of them for the total'''

        for i in range(len(movie_price)):
            print(movie_price[i])
                
        # calculates the total
        print('Your total is: $', sum(movie_price))

    def purchase_history(all_collected):
        '''The for loop grabs values from the all_collected list and prints them out.'''

        for i in range(len(all_collected)): #prints out everything in the all_collected list
            print(all_collected[i])


            
def main():

    rented_movies = [] # list to record the rented movies
    list_position = [0]*50 # list to record the places of the movies in the rented list
    all_collected = [] # the list for all movies ever rented and won't have movies removed from it with the return function
    movie_price = [] # holds every price for the rented_movies.

    # while loop for the code to keep on running.
    while len(rented_movies)-1 <= 50:

        user_choice = input("\n \nMenu: \n To see the rentable movies, type 'movie list' \n To rent a movie, type 'rent' \n To return a movie, type 'return' \n To see all of the movies you have currently rented, type 'view all' \n To view your purchase history, type 'history' \n To get the total of the movies you are currently renting, type 'receipt' \n ")

        # EXECUTE if the user wants to see the movie list
        if user_choice == 'movie list':

            # opens the file with the movie list and prints every line out with the for loop
            with open('rentablemovieslist.txt', 'r') as f:
                for line in f:
                    print(f.readline(), end="")

        # EXECUTE if the user asks to rent a movie
        elif user_choice == 'rent':
            # as the movie is being rented, this prepares the list where the prices will be recorded
            with open('pricelist.txt', 'r') as r:

                price = r.readlines()
                new_price = [] # list for every movie's monthly price

                # for loop to get rid of the backslash n
                for i in price:
                    if i[-1] == '\n':
                        new_price.append(i[:-1]) # adds the modified element to the new list
                    else:
                        new_price.append(i)

                # rentable movie list file         
                with open('rentablemovieslist.txt', 'r') as f:

                    word = f.readlines() # assigns the entire rentablemovieslist.txt to a variable
                    new_word = [] # the new list for the words without the back slash n.

                    # for loop to make the new list without the backslash n.
                    for line in word:
                        if line[-1] == '\n': # excludes the last 2 characters
                            new_word.append(line[:-1]) 
                        else:
                            new_word.append(line)

                    
                    movie_choice = input("Which movie would you like to rent? ") # asks for the movie that the user wants to rent
                    
                    # for loop to search for the movie in the new word list.
                    for i in range(len(new_word)):
                        if new_word[i] == movie_choice:
                            print("You have successfully rented", movie_choice,'!')

                            # add the movie to the list of the rented movies
                            rented_movies.append(movie_choice)

                            # add the position of the movie in the list to another list
                            list_position[i] = i

                            # add the movie to the non-removable movie list
                            all_collected.append(movie_choice)

                            # movie prices
                            movie_price.append(new_price[i]) # adding the price of a movie to the same list position
                            #movie_price = [float(i) for i in movie_price] # converts the list elements into floats
                        else:
                            pass


        # EXECUTE if the user wants to return a movie
        elif user_choice == 'return':

            movie_remove = input("Which movie would you like to remove? ") # the user input for the movie they want to return

            # checks to see if the rented_movie list has any elements in it before it starts the loop
            if len(rented_movies) != 0:

                # for loop to remove the movie title from the rented_movie list and the price from the new_price list
                for i in range(len(rented_movies)):
                    if movie_remove == rented_movies[i]:
                        rented_movies.remove(rented_movies[i])
                        movie_price.remove(movie_price[i])
                        
                        print('[You have returned the movie', movie_remove, '.]')

                    else:
                         
                        # warns user that the output is invalid with a pop-up
                        invalid_output = Tk()
                        invalid_output.configure(background='white')
                        invalid_output.title("Error")
                        ttk.Label(invalid_output, text='[You have not rented this movie, so you cannot return it.]').grid(column=0, row=0)
                        print("[You have not rented this movie, so you cannot return it.]")
            
            else:
                # warns user that the output is invalid with a pop-up
                invalid_output = Tk()
                invalid_output.configure(background='white')
                invalid_output.title("Error")
                ttk.Label(invalid_output, text="[You haven't rented any movies, failed action.]").grid(column=0, row=0)
                print("[You haven't rented any movies, failed action.]")

        # EXECUTE if the user wants to view all the movies they have rented
        elif user_choice == 'view all':
            
            # value checker using list length
            if len(rented_movies) != 0:    
                for i in range(len(rented_movies)):
                    print(rented_movies[i])

            else:
                # warns user that the output is invalid with a pop-up
                invalid_output = Tk()
                invalid_output.configure(background='white')
                invalid_output.title("Error")
                ttk.Label(invalid_output, text='[Rented Movies List empty.]').grid(column=0, row=0)
                print("[Rented Movies List empty.]")

        # EXECUTE if the user wants to view their purchase history
        elif user_choice == 'history':

            # value checks to see if the list is empty or not before starting the program.
            if len(all_collected) != 0:

                movie_history = Movies.purchase_history(all_collected) # variable with parameters
                print(Movies.purchase_history(movie_history)) # mini class displays every movie that the user has rented in the past

            else:
                invalid_output = Tk()
                invalid_output.configure(background='white')
                invalid_output.title("Error")
                ttk.Label(invalid_output, text='[Your purchase history is empty.]').grid(column=0, row=0)
                print('[Your purchase history is empty.]')

        # EXECUTE if the user wants to view the total for the movies they are currently renting
        elif user_choice == 'receipt':

            # value checks to see if the list is empty or not before starting the program.
            if len(movie_price) != 0:
                total = Movies.receipt(movie_price) # variable with the parameters
                print(Movies.receipt(total)) # mini class displays the total price for the user to pay

            else:
                invalid_output = Tk()
                invalid_output.configure(background='white')
                invalid_output.title("Error")
                ttk.Label(invalid_output, text='[You havent purchased anything yet.]').grid(column=0, row=0)
                print('[You havent purchased anything yet.]')
                        

        # EXECUTE if the user gives an invalid input that isn't one of the options
        else:

            # warns user that the output is invalid with a pop-up
            invalid_output = Tk()
            invalid_output.configure(background='white')
            invalid_output.title("Error")
            ttk.Label(invalid_output, text='Invalid Output').grid(column=0, row=0)
            print("Invalid Output")


main()    
    
