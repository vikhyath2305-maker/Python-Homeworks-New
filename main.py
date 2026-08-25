import csv

shopping_list = ['apple', 'banana', 'carrot']

with open('shopping_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(shopping_list)

loaded_list = []

with open('shopping_list.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for item in row:
            loaded_list.append(item)

print(loaded_list)