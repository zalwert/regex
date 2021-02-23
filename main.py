import re


# Example 1: finding e-mails in text
example_string = 'This is example string with example@example.com mail ' \
    'and with example-example@example.com.'

all_emails = re.findall(r'[\w.-]+@[\w.-]+.\w+', example_string)

print(all_emails)

# Example 2:
# Example 3:
# Example 4:
# Example 5:
