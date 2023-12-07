import re

password = "2a#"
x = re.search("^![a-z]+[0-9]+$", password)

if x is None:
    print("Invalid password")
else:
    print("Valid password")
