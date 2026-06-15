def table(number, limit=10):
    print(f"Multiplication table of {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))
table(number)