import time

print("****************************************");
print("*****Welcome to the Calculator Menu*****");
print("****************************************");
print();

print("This calculator will contain:"); time.sleep(2);
print("1. Normal Calculator"); time.sleep(1);
print("2. Conversion Calculator"); time.sleep(1);
print();

num1 = int(input("Select which calculator you would like to use: ")); time.sleep(1);

if num1 == 1:
    import calculator

if num1 == 2:
    import conversion
