#FizzBuzz Function using loop
def fizzBuzz(i):
    for i in range(1, 51):
        if i % 3 is 0 and i % 5 is 0:
            print("FizzBuzz")
        elif i % 3 is 0:
            print("Fizz")
        elif i % 5 is 0:
            print("Buzz")
        else:
            print(i)
i = 1
fizzBuzz(i)