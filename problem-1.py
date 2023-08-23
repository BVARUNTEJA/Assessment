import re

def check(contact_number):
    pattern = r'^(\+\d{1,2}\s?)?(\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    return re.match(pattern, contact_number)

n=int(input())#enter the no.of mobile_number that we want to check
#enter the mobile numbers
contact_numbers=[input() for i in range(n)]
for i in contact_numbers:
    if check(i):
        print("The entered mobile_number is vaild")
