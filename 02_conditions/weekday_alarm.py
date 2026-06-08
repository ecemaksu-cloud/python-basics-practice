# Set alarm according to the day of the week

day = input("Enter the day: ").lower()

if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Alarm set for 07:00")
elif day in ["saturday", "sunday"]:
    print("Alarm set for 09:30")
else:
    print("Invalid value entered")
