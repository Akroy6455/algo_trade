import csv

def csv_to_int_list(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Remove brackets, convert to integer
        return [float(item[0].strip('[]')) for item in csv_reader]

# Assign the result to a variable
my_data = csv_to_int_list('niftynidhi.csv')

# Now my_data is a list of integers
# For example, to print the first item:
print(my_data[0])

# You can also perform integer operations
#print(my_data[1] + 5)  # This will work because my_data[0] is an integer