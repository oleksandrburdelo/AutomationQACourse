names_1 = {'John Dow', 'Marta Dow', 'John Travolta', 'Marta Onischuk', 'Marta', 'John Dow'}
names_2 = {'John Travolta', 'Oleksandr Burdelo', 'Marta', 'Marta Onischuk', 'John Dow'}
print(names_1.intersection(names_2))

# Not correct. Main idea of this task is to get all names which unique.
# For example if I have list ["John", "Marta", "James", "John"] and you should
# get only unique of them. It means that "John" will be only one.
# ["John", "Marta", "James", "John"] => ["John", "Marta", "James"]
# Set it is not the best type for this task.
