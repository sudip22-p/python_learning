import re

# Common Functions
# Function	        Purpose
# re.match()	    Match pattern at the start of string
# re.search()	    Search for first occurrence in string
# re.findall()	    Find all matches
# re.sub()	        Substitute one pattern with another
# re.compile()	    Compile regex for reuse


# Common Patterns
# Pattern	        Meaning
# .         	Any character except newline
# \d	        Digit (0–9)
# \D	        Non-digit
# \w	        Word char (a-z, A-Z, 0–9, _)
# \W	        Non-word character
# \s	        Whitespace
# \S	        Non-whitespace
# ^	            Start of string
# $	            End of string
# [...]	        Set of characters
# [^...]	    Not in set
# *	            0 or more
# +	            1 or more
# ?	            0 or 1
# {n}	        Exactly n times
# {n,m}	        Between n and m times
# (...)	        Grouping


text = "My email is sud22@gmail.com and I am 22 years old. Contact: +977-9812345678. My phone number is +1-123-456-7890."


# Match at start of string here r is a raw string that prevents escape sequences(\) from being processed.
print(re.match(r"My", text))  # Match object

# Search: first match anywhere
match = re.search(r"\d+", text)  # First number
print(
    "First number:", match.group()
)  # 22 if there we use as \d then it will return the first digit

# Find all numbers
numbers = re.findall(r"\d+", text)
print("All numbers:", numbers)

# Replace all digits with '#'
cleaned = re.sub(r"\d", "#", text)
print("Digits replaced:", cleaned)

# Compile a regex pattern (for reuse)
# text = "cat scat category"

# # Without \b (word boundary)
# # Matches 'cat' anywhere in the text: even inside 'scat' and 'category'
# print(re.findall(r"cat", text))
# # Output: ['cat', 'cat', 'cat']

# # With \b at beginning and end: \bcat\b
# # \b matches a word boundary (before/after a word)
# # So it matches only the standalone word 'cat'
# print(re.findall(r"\bcat\b", text))
# # Output: ['cat']

pattern = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
email = pattern.search(text)
print("Email found:", email.group())

# Using groups
phone = re.search(r"(\+\d{1,2})-(\d{3})-(\d{3})-(\d{4})", text)
if phone:
    print("Country Code:", phone.group(1))
    print("Full Phone:", phone.group())

# Character sets and boundaries
words_with_digits = re.findall(r"\b\w*\d\w*\b", text)
print("Words containing digits:", words_with_digits)

# Optional match
optional = re.search(r"Email:? (\w+@\w+\.\w+)?", "Email: test@mail.com")
print("Optional email:", optional.group())

# Anchors: ^ for start, $ for end
starts_with_my = re.match(r"^My", text)
print("Starts with 'My':", bool(starts_with_my))

ends_with_digit = re.search(r"\d$", "Ends with 9")
print("Ends with digit:", bool(ends_with_digit))


# # re.match() checks only the start, so '^' is optional
print(re.match(r"My", text))  #  Matches 'My'
print(re.match(r"^My", text))  #  Same result as above

# # re.search() checks anywhere, so '^' anchors to start
print(re.search(r"^My", text))  #  Matches only if 'My' is at the beginning
print(re.search(r"My", text))  #  Matches 'My' anywhere in the string
