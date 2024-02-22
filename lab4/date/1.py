from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days
result_date = current_date - timedelta(days=5)

# Print the result
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Subtracted 5 days:", result_date.strftime("%Y-%m-%d"))