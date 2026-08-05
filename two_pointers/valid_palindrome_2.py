def is_palindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        # char is not alpha
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True


s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
