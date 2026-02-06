#1.Mario Pyramid of list 

height = 5
pyramid = []

for i in range(1, height + 1):
    row = [' '] * (height - i) + ['*'] * i
    pyramid.append(row)

for row in pyramid:
    print(row)

#2.function that validate email and takes list of emails 

emails = [
    "aya@gmail.com",
    "user.name@gmail.com",
    "user123@gmail.com",
    "ayagmail.com",
    "aya@gmail",
    "aya@.com",
    "aya@com.",
    "@gmail.com",
    "aya@gmail.",
    "aya@ gmail.com",
    "",
    "   ",
]

def is_valid_email(email):
    return email != "" and "@" in email and "." in email.split("@")[-1] and email.endswith("gmail.com")

valid_emails = list(filter(is_valid_email, map(str.strip, emails)))
print(valid_emails)





