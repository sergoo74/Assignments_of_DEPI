## 1. Strings:
# Question 1 :
# Write a Python program that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in the sentence.
# Example:
from operator import index
x="Hello World"
y=3
print(x)  #Hello World
print(y)  #3
## 2. Lists:
# Question 2 :
# Given a list of numbers [1, 3, 5, 7, 9], write a Python program to double each element in the list and store the result in a new list.
# Example:
num=[1, 3, 5, 7, 9]
Result=[x*2 for x in num ]
print(Result) #num *2
## 3. Sets:
# Question 3 :
# Create two sets: set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}. Write a Python program to find the union and intersection of the two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2)) # set1 + set2
print(set1|set2) #set1 + set2
print(set1.intersection(set2)) # Similar Between Sets
## 4. Dictionaries:
# Question 4 :
# Given a dictionary {'a': 1, 'b': 2, 'c': 3}, write a Python program to swap the keys and values, so the resulting dictionary becomes {1: 'a', 2: 'b', 3: 'c'}.
original_dictionary={'a': 1,'b': 2,'c': 3}
sawpe_dictionary={}
for key ,vaule in original_dictionary.items():
    sawpe_dictionary[vaule]=key
    print(f"Origial_dictionary: ", original_dictionary) #{'a': 1,'b': 2,'c': 3}
    print(f"Updated_dictionary: ",sawpe_dictionary) #{1: 'a', 2: 'b', 3: 'c'}
## 5. Tuples:
# Question 5 :
# Given a tuple (5, 10, 15, 20), write a Python program to convert it into a list, change the second element to 12, and then convert it back to a tuple.
Num=(5, 10, 15, 20)
a=list(Num)
a[1]=12
Updated_tuple=tuple(a)
print(Updated_tuple)
## 6. Functions:
# Question 6 :
# Write a Python function named is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
def is_apalindrome(object):
    object=object.strip().lower()
    return object==object[::-1]
print(is_apalindrome("radar"))#True
print(is_apalindrome("hello"))#False
## 7. Functions:
# Question 7 :
# Write a Python function named count_occurrences that takes two arguments: a list of integers and a target integer. The function should return a dictionary where the keys are the unique integers from the list, and the values are the number of times each integer occurs in the list. Additionally, if the target integer is present in the list, the function should also include the key "target_count" with its value being the number of times the target integer occurs.
def count_occurrences(numbers, target):
    occurrences={}
    for num in numbers:
        if num in occurrences:
            occurrences[num]+=1
        else:
            occurrences[num]=1
    if target in occurrences:
        occurrences["target_count"]=occurrences[target]
        return occurrences
print(count_occurrences([1,2,2,3,4,2,5],2))#{1: 1, 2: 3, 3: 1, 4: 1, 5: 1, 'target_count': 3}
print(count_occurrences([10,10,20,30],10))# {10: 2, 20: 1, 30: 1, 'target_count': 2}
## 8. while loop:
# Write a Python program that uses a while loop to generate a sequence of numbers starting from 1. The loop should continue generating numbers and adding them to a list until the sum of all numbers in the list exceeds 200. After the loop, print the list of numbers and the total sum of the numbers.
numbers=[]
total_sum=0
num=1
while total_sum<200:
    numbers.append(num)
    total_sum+=num
    num+=1
print("List of numbers" , numbers)# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Total sun of numbers",total_sum)#210

## 9. Question:
# Write a Python function named remove_duplicates that takes a list of integers as input and returns a new list with duplicate values removed.
# The order of the original list should be preserved in the new list.
def remove_duplicates(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers
print(remove_duplicates([5, 5, 5, 2, 2, 3, 4, 4, 5]))#[5, 2, 3, 4]
## 10. Question:
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
## Other Soulation
def my_fruits(fruits):
    fruits_dict={}
    for index,fruit in enumerate(fruits):
        if fruit in fruits_dict:
            fruits_dict[fruit].append(index)
        else:
            fruits_dict[fruit]=[index]

    return fruits_dict

list_fruit=["apple", "banana", "orange", "banana", "kiwi", "apple"]
print(my_fruits(list_fruit)) #{'apple': [0, 5], 'banana': [1, 3], 'orange': [2], 'kiwi': [4]}