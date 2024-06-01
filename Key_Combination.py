def letter_combinations(digits):
    if not digits:
        return []
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    result = []

    def backtrack(index,current_combination):
        if index == len(digits):
            result.append("".join(current_combination))
            return
        current_digit = digits[index]
        for letter in phone_map[current_digit]:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            current_combination.pop()
    backtrack(0,[])
    return result
print(letter_combinations("23"))
print(letter_combinations(""))
print(letter_combinations("2"))