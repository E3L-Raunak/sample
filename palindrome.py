def is_palindrome(s):
    s = s.replace("\s", "").lower()
    return s == s[::-1]

# Example usage:
word = 'A man a plan a canal Panama'
if is_palindrome(word):
    print(f'{word} is a palindrome.')
else:
    print(f'{word} is not a palindrome.')