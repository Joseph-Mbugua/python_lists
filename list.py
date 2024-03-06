import time

# Task 1: Accept user input to create a list of integers and compute their sum
print("This program accepts user input to create a list of integers and then computes the sum of all the integers in the list.")
time.sleep(3)
input("Press Enter to continue...")
num_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
sum_of_integers = sum(num_list)
print("Sum of integers:", sum_of_integers)

time.sleep(3)
print("This program creates a tuple containing the names of five favorite books and uses a for loop to print each book name on a separate line.")
# Task 2: Create a tuple containing the names of five favorite books and print them using a for loop
time.sleep(3)
input("Press Enter to continue...")
favorite_books = ("River and The Source", "Enemy of The People", "My Life in Crime", "Sinisters Trophy", "The Girl was Mine")
print("Favorite Books:")
for book in favorite_books:
    print(book)
time.sleep(3)


# Task 3: Use a dictionary to store information about a person and print it
print("This program utilizes a dictionary to store information about a person, including their name, age, and favorite color. It prompts the user for input and stores the information in the dictionary, then prints the dictionary to the console.")
time.sleep(3)
input("Press Enter to continue...")
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
print("Person's Information:", person)
time.sleep(3)


# Task 4: Accept user input to create two sets of integers and find their common elements
print("This program accepts user input to create two sets of integers and creates a new set that contains only the elements that are common to both sets."

)
time.sleep(3)
input("Press Enter to continue...")
set1 = set(map(int, input("Enter elements of set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set 2 separated by spaces: ").split()))
common_elements = set1&(set2)
print("Common elements:", common_elements)
time.sleep(3)

# Task 5: Store a list of words and create a new list with words having odd number of characters
print("This program stores a list of words and then uses list comprehension to create a new list that contains only the words with an odd number of characters."




)
time.sleep(3)
input("Press Enter to continue...")
word_list = ["apple", "google", "microsoft", "safaricom", "Facebook", "linux"]
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
even_length_words = [word for word in word_list if len(word) % 2 == 0]
print("Words with odd number of characters:", odd_length_words)
print("Words with even number of characters:", even_length_words)
