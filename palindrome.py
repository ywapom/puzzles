
words = ['cat', 'dad', 'mom', 'madam', 'mongo']

def IsPalindrome(_word):
    #rev = _word[::-1]
    rev = ''.join(reversed(_word))
    return rev == _word

for word in words:
    result = IsPalindrome(word)
    print(f"{word} is a palindrome?: {result}")
