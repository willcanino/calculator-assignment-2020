print("**********************************");
print("*****Welcome to my Calculator*****");
print("**********************************");
print();

num1 = input("Enter your first number: ");
num2 = input("Enter your second number: ");

num1 = int(num1);
num2 = int(num2);

while True:
  operator = input("What operator do you want to use? [ + | - | * | / ]");

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
    continue

  print(f"{num1} {operator} {num2} = {result}");

  num1 = result

  response = input("Do you want to run another calculation? [Y/N]");
  if response == "n" or response == "N" or response == "no" or response == "No":
    print()
    print("Thank you for using this calculator! :)");
    break
  num2 = input("Enter your next number: ");
  num2 = int(num2);
