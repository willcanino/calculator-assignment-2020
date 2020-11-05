import time

print("**********************************************");
print("*****Welcome to the Conversion Calculator*****");
print("**********************************************");
print();
first = True
while True:
    if not first:
        again = input("Would you like to run another equation?")
        if again == "no" or again == "No":
            break
        print("These are the following Conversions?"); time.sleep(1);
        print("1. Fahrenheit to Celsius"); time.sleep(1);
        print("2. Celsius to Fahrenheit"); time.sleep(1);
        print("3. Miles to Kilometers"); time.sleep(1);
        print("4. Kilometers to Miles"); time.sleep(1);
        print();

        num1 = int(input("Which conversion would you like to use: ")); time.sleep(1);

        if num1 == 1:
            fah = int(input("Enter your number in Fahrenheit: ")); time.sleep(1);
            cel = (fah - 32)*5/9;
            print("The temperature in Degrees Celsius is: ", cel); time.sleep(1);

        if num1 == 2:
            cel = int(input("Enter your number in Degrees Celsius: ")); time.sleep(1);
            fah = (cel*9/5)+32;
            print("The temperature in Fahrenheit is: ", fah); time.sleep(1);

        if num1 == 3:
            m = int(input("Enter your number in Miles: ")); time.sleep(1);
            km = (m*1.609);
            print(m, "Miles is", km, "Kilometers (approximately)"); time.sleep(1);

        if num1 == 4:
            km = int(input("Enter your number in Kilometers: ")); time.sleep(1);
            m = (km/1.609);
            print(km, "Kilometers is", m, "Miles (approximately)"); time.sleep(1);
        
        first = False
