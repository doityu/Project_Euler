#### パクリ

n = 1000

numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
           16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
           30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
           80: "eighty", 90: "ninety", 1000: "one thousand"}


def number_to_word(num):
    if num in numbers:
        return numbers[num]
    elif num < 100:
        a = num % 10
        b = (num // 10) * 10
        return number_to_word(b) + "-" + number_to_word(a)
    else:
        a = num % 100
        b = num // 100
        if a == 0:
            return number_to_word(b) + " hundred"
        else:
            return number_to_word(b) + " hundred and " + number_to_word(a)


def to_character_num(word):
    return len(word.replace(" ", "").replace("-", ""))


seq = range(1, n+1)
words = map(number_to_word, seq)
result = sum(map(to_character_num, words))

print(words)
print(result)
