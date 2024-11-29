## 1
from unittest import removeResult
## Question 1:
# Write a Python function called greet_user that takes two parameters: name (a string representing the user's name) and greeting (a string representing a greeting message). The function should print the personalized greeting message.
# If the greeting parameter is not provided, the function should use "Hello" as the default greeting.
# Expected Output:
# If the user's name is "Alice" and no specific greeting is provided, the function should print "Hello, Alice!".
# Please write the Python code for the greet_user function and demonstrate its usage with different examples, both with and without a specific greeting
def greet_user(name,greeting='Hello'):
    print(f"{greeting} , {name}!")
greet_user("Alice" ) #Hello , Alice!
greet_user("Alice" , "Good morning")#Good morning , Alice!
greet_user("Bob", "Hi There")#Hi There , Bob!
## 2
## Question 2:
# Write a Python program that takes two tuples as input, each containing integers, and returns a new tuple containing the element-wise sum of the corresponding elements from the input tuples. Assume the input tuples have the same length.
# Expected Output:
# If the input tuples are (1, 2, 3) and (4, 5, 6), the program should return (5, 7, 9).
# Please write the Python code to accomplish this task.
def sum_tuple(tuple1,tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Both Tuple must have the same length ")
    else:
        result=tuple(a+b for a , b in zip(tuple1,tuple2))
        return result
tuple1=(1,2,3)
tuple2=(4,5,6)
result=sum_tuple(tuple1, tuple2)
print(result)# sum_tuples(5, 7, 9)
## 3
## Question 3:
# Write a Python program that prompts the user to guess a secret number between 1 and 10. The program should continue to prompt the user for guesses until they correctly guess the secret number. Provide feedback to the user if their guess is too high or too low.
# Expected Output:
# If the secret number is 7 and the user's guesses are 5, 8, 7, the program should print:
# "Too low! Try again."
# "Too high! Try again."
# "Congratulations! You guessed the secret number 7."
# Please write the Python code for this guessing game using a while loop.
secret_number=7
print("Guess the secert number between 1 and 10!" )
while True:
    try:
        guess=int(input("Enter Your Guess:"))
    except ValueError:
        print("invalid")
        continue
    if guess<secret_number:
        print("Too low! Try again")
    elif guess>secret_number:
        print("Too High! Try again")
    else:
        print(f"Congratulations you guessed the secert number {secret_number}")
        break
## 4
## Question 4:
# Write a Python program that takes a list of words as input and creates a dictionary where the keys are the unique words in the list, and the values are lists containing the indices (positions) at which each word appears in the list.
# Expected Output:
# If the input list is ["apple", "banana", "orange", "banana", "kiwi", "apple"], the program should return {'apple': [0], 'banana': [1], 'orange': [3], 'kiwi': [4]}.
# Please write the Python code to accomplish this task.
def  dic_1(in_list):
    if type(in_list)!=list:
        print(f"{in_list} Not a List ")
    else:
        in_dict={}
    for index , val in enumerate(in_list):
        if val in in_dict:
            continue
        else:
            in_dict.update({val:index})
    return in_dict
my_list=["apple", "banana", "orange", "banana", "kiwi", "apple"]
print(dic_1(my_list)) #{'apple': 0, 'banana': 1, 'orange': 2, 'kiwi': 4}