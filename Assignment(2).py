#1
### Question: Extract and Analyze List Slices
# **Description:**
# Given a list of tuples,where each tuple contains information about a product (product name, price, and quantity), write a program that extracts the product names and prints the names of products with prices above a certain threshold using list slicing and if statements.
# The threshold should be set within your code.
products = [
    ("Laptop", 1200, 5),
    ("Smartphone", 700, 10),
    ("Headphones", 150, 15),
    ("Monitor", 300, 7)
]
threshold = 500
above_threshold=[product[0] for product in products if product[1]> threshold]

print(f"Products above the price threshold:{above_threshold}") #Products above the price threshold
#2
### Question: Update Dictionary with Tuple Data
# Description:
# You have a dictionary where keys are employee IDs and values are their current salaries. You also have a list of tuples where each tuple contains an employee ID and a percentage increment to their salary.
# Write code to update the salaries in the dictionary based on the increment provided in the list of tuples.
# Use if statements to ensure that only existing employees in the dictionary are updated.
salaries = {
    101: 50000,
    102: 60000,
    103: 55000
}
increments = [
    (101, 10),  # 10% increment
    (104, 5),   # 5% increment, not in salaries
    (102, 15)
]
for employer,increment in increments:
    if employer in salaries:
        salaries[employer] +=salaries[employer] *(increment/100)
print(f"Updated salaries: {salaries}") #Updated salaries

