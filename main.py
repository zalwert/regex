import re

example_string = 'This is example string with example@example.com mail ' \
    'and with example-example@example.com.'

all_emails = re.findall(r'[\w.-]+@[\w.-]+.\w+', example_string)

print(all_emails)
