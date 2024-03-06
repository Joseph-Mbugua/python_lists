# Task 1: Accept user input to create a list of integers and compute their sum
num_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
sum_of_integers = sum(num_list)
print("Sum of integers:", sum_of_integers)

# Task 2: Create a tuple containing the names of five favorite books and print them using a for loop
favorite_books = ("Book1", "Book2", "Book3", "Book4", "Book5")
print("Favorite Books:")
for book in favorite_books:
    print(book)

# Task 3: Use a dictionary to store information about a person and print it
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
print("Person's Information:", person)

# Task 4: Accept user input to create two sets of integers and find their common elements
set1 = set(map(int, input("Enter elements of set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set 2 separated by spaces: ").split()))
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)

# Task 5: Store a list of words and create a new list with words having odd number of characters
word_list = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
