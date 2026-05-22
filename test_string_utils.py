import pytest
from string_utils import reverse_words, count_vowels, is_palindrome

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("") == ""
    assert reverse_words("hello") == "hello"

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("") == 0

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True