print("**********************************");
print("*****Welcome to my Calculator*****");
print("**********************************");
print();

# Take initial numbers from the user
num1 = input("Enter your first number: ");
num2 = input("Enter your second number: ");

# Convert the text (str) we got from the user to an int
num1 = int(num1);
num2 = int(num2);

while True:
  operator = input("What operator do you want to use? [ + | - | * | / ]");

  # These if statements determine what operator the user inputted
  if operator == '+':
    result = num1 + num2
  elif operator == '-':
    result = num1 - num2
  elif operator == '*':
    result = num1 * num2
  elif operator == '/':
    result = num1 / num2
  else:
    print(f"{operator} is an invalid operator");
    # This skips the rest of lines of code in the loop and starts at the
    # beginning
    continue

  # print out the result
  print(f"{num1} {operator} {num2} = {result}");

  # We need to set num1 = result so that when the loop repeats the if statement
  # the result we be passed along instead of just using the old num1 value
  # in the computation
  num1 = result

  response = input("Do you want to run another calculation? [Y/N]");
  if response == "n" or response == "N" or response == "no" or response == "No":
    # This stops the loops
    print()
    print("Thank you for using this calculator! :)");
    break
  # This must be set to num2 in order for the if statements above to work
  num2 = input("Enter your next number: ");
  # Convert num2 from a str to an int
  num2 = int(num2);
