from typing import List

def fizz_buzz(n: int) -> List[str]:
    result = []
    for i in range(1,n +1):
        if i % 3 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

n = 20
output = fizz_buzz(n)
for line in output:
    print(line)