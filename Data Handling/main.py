# Homework: Number List and Dictionary Statistics
# This program takes numbers from the user, stores them in a list
# and a dictionary, then calculates the sum, average, max, and min.

# Step 1: Get numbers from the user
while True:
    user_input = input("Enter numbers separated by spaces: ")

    try:
        number_list = []

        for num in user_input.split():
            number_list.append(float(num))

        break

    except ValueError:
        print("Invalid input! Please enter numbers only.")

print("\nYour list of numbers:", number_list)

# Step 3: Build a dictionary that stores each number and how many times it appears
number_dict = {}
for num in number_list:
    if num in number_dict:
        number_dict[num] += 1
    else:
        number_dict[num] = 1

print("Number frequencies:", number_dict)

# Step 4: Calculate basic statistics
total_sum = sum(number_list)
average = total_sum / len(number_list)
max_value = max(number_list)
min_value = min(number_list)

# Step 5: Print the results
print("\n--- Statistics ---")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
