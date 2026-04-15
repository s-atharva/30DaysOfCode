def is_palindrome(s: str) -> bool:
    clearned = ''
    for char in s:
        if char.isalnum():
            clearned += char.lower()
    return clearned == clearned[::-1]


def is_palindrome_optimal(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


my_string = 'tooT'
print(is_palindrome(my_string))
print(is_palindrome_optimal(my_string))
