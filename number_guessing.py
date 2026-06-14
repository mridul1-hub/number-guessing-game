print("Enter the range (Integers only):")

first = int(input("Enter your first number = "))
last = int(input("Enter your last number = "))

print(f"Assuming your number lies between {first} and {last}")

while first <= last:
    mid = (first + last) // 2

    temp = input(f"Is your number {mid}? (yes/less/more) = ").lower()

    if temp == "yes":
        print(f"I guessed it right! It's {mid}")
        break

    elif temp == "less":
        last = mid - 1

    elif temp == "more":
        first = mid + 1

    else:
        print("Please enter only yes, less, or more.")

else:
    print("Your answers are inconsistent. You may have changed the number.")