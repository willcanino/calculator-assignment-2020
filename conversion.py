import time

print("**********************************************");
print("*****Welcome to the Conversion Calculator*****");
print("**********************************************");
print();

print("Which conversion would you like to do?"); time.sleep(1);
print("1. Fahrenheit to Celsius"); time.sleep(1);
print("2. Celsius to Fahrenheit"); time.sleep(1);
print("3. Miles to Kilometers"); time.sleep(1);
print("4. Kilometers to Miles"); time.sleep(1);

num1 = int(input("Which conversion would u like: ")); time.sleep(1);

if num1 == 1:
    cel = int(input("Enter your number in Degrees Celsius: ")); time.sleep(1);
    fah = (cel*9/5)+32;
    print("The temperature in Fahrenheit is: ", fah);

if num1 == 2:
    fah = int(input("Enter your number in Fahrenheit: ")); time.sleep(1);
    cel = (fah - 32)*5/9;
    print("The temperature in Degrees Celsius is: ", cel);

if num1 == 3:
    km = int(input("Enter your number in Kilometers: ")); time.sleep(1);
    m = (km*1.609);
    print(km, "Kilometers is", m, "Miles (approximately)");

if num1 == 4:
    int(input("Enter your number in Kilometers: ")); time.sleep(1);
