def reverse_words(text: str) -> str:
    """反转字符串中单词的顺序。
    
    例如: "hello world" -> "world hello"
    空字符串返回空字符串。
    """
    words = text.split()
    return " ".join(words[::-1])


def count_vowels(text: str) -> int:
    """统计字符串中元音字母的数量（不区分大小写）。
    
    例如: "Hello" -> 2 (e, o)
    空字符串返回 0。
    """
    return sum(1 for letter in text if letter.lower() in "aeiou")


def is_palindrome(text: str) -> bool:
    """判断字符串是否为回文。
    
    例如: "racecar" -> True, "hello" -> False
    空字符串返回 True。
    """
    return text == text[::-1]