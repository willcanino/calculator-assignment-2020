import time

print("***************************************************");
print("*****Welcome to the Time Conversion Calculator*****");
print("***************************************************");
print();

print("These are the following Conversions allowed: ");
print("1. Seconds to Minutes");
print("2. Minutes to Seconds");
print("3. Seconds to Hours");
print("4. Hours to Seconds");
print("5. Seconds to Days");
print("6. Days to Seconds");
print("7. Seconds to Weeks");
print("8. Weeks to Seconds");
print("9. Years to Seconds");
print("10. Seconds to Years");
print("11. Seconds to Decades");
print("12. Decades to Seconds");
print("13. Centurys to Seconds");
print("14. Minutes to Hours");
print("15. Hours to Minutes");
print("16. Minutes to Days");
print("17. Days to Minutes");
print("18. Minutes to Weeks");
print("19. Weeks to Minutes");
print("20. Minutes to Months");
print("21. Months to Minutes");
print("22. Minutes to Years");
print("23. Years to Minutes");
print("24. Minutes to Decades");
print("25. Decades to Minutes");
print("20. Minutes to Centurys");
print("20. Centurys to Minutes");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");
print("20. Minutes to Months");

num1 = int(input("Enter which time conversion you would like to use: "));

if num1 == 1:
    sec = int(input("Enter the amount of seconds you would like to convert to minutes: "));
    min = (sec/60);
    print(sec,"seconds is", min,"minutes.");

if num1 == 2:
    min = int(input("Enter the amount of minutes you would like to convert to seconds: "));
    sec = (min*60);
    print(min,"minutes is",sec,"seconds.")

if num1 == 3:
    sec = int(input("Enter the amount of seconds you would like to convert to hours: "));
    hrs = (sec*3600);
    print(sec,"seconds is",hrs,"hours")
