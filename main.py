import re


# Example 1: finding e-mails in text
example_string = 'This is example string with example@example.com mail ' \
    'and with example-example@example.com.'

all_emails = re.findall(r'[\w.-]+@[\w.-]+.\w+', example_string)

print(all_emails)

# Example 2:
example_string2 = 'Welcome to this tutorial website. This is your first article. Learn and learn, then start using! ' \
                  ' www.google.com, www.google.co.fr'

all_links = re.findall(r'\bwww.[\w.-]+', example_string2)

print(all_links)

# Example 3:
example_string3 = 'This are a few numbers like: 999 443 221 & 333 232 123. Find them all!'

all_numbers = re.findall(r'[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]', example_string3, re.DEBUG)

print(all_numbers)

# Example 4:
example_string4 = "She is extremely intelligent and she have a lovely voice - her name Molyna"
pattern = r"\w+ly\b"
for m in re.finditer(pattern, example_string4):
    print(f'{m.start():02d}-{m.end():02d} {m.group(0):s}')

# Example 5:
re.split(r'\W+', '1word, 2word, third&word. | word#@word')