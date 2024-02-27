def all_true(tuple_values):
    return all(tuple_values)

# Example usage
my_tuple1 = (True, True, True)
my_tuple2 = (True, False, True)

print(all_true(my_tuple1))  # Output will be True
print(all_true(my_tuple2))  # Output will be False
