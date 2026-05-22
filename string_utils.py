def reverse_words(s):
    words = s.split()
    rwords = words[::-1]
    return " ".join(rwords)
def count_vowels(s):
    count = 0
    for letter in s:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
def is_palindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    else:
        return False