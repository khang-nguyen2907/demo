import re
username = input("Enter your username: ")
password = input("Enter your password: ")

password_lst = password.strip().split(',')
valid_password = list()

for i in password_lst:
    lower, digit, upper, spec, length = False, False, False, False, False
    p = i.strip()
    if re.search(".*[a-z]+.*", p):
        lower = True
    if re.search(".*[0-9]+.*", p):
        digit = True
    if re.search(".*[A-Z]+.*", p):
        upper = True
    if re.search(".*[$#@]+.*", p):
        spec = True
    if len(p) >= 6 and len(p)<= 12:
        length = True
    if lower and digit and upper and spec and length:
        valid_password.append(p)

if len(valid_password) > 0:
    print("\nValid password: ")
    print(",".join(valid_password))
else:
    print("\nThere is no any valid password.")

#GiaKhang@29, giakhang@K, Khang