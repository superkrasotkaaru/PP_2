from datetime import datetime

# Enter two dates as strings in the format 'YYYY-MM-DD HH:MM:SS'
date_str1 = '2022-01-01 12:00:00'
date_str2 = '2022-02-01 18:30:00'

# Convert the date strings to datetime objects
date1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')

# Calculate the difference in seconds
time_difference_seconds = (date2 - date1).total_seconds()

# Print the result
print(f"The difference between the two dates is {time_difference_seconds} seconds.")