import string
import secrets

print("\033[34m")
print(r"""
██╗  ██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗
╚██╗██╔╝██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
 ╚███╔╝ ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
 ██╔██╗ ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██╔╝ ██╗╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ By ABX
""")
print("\033[0m")

passwordrange = input("\033[35mPlease put the password words range: \033[0m")
choise = input("""\033[32m======================================Select an option============================================\033[0m
\033[33m1. Password With upper letters, lower letters, Numbers and Special Characters(Recommended)
2. Password With upper letters, lower letters and Numbers only
3. Password With upper letters and lower letters only
4. Password With upper letters only
5. Password With lower letters only\033[0m
\033[32m=================================================================================================\033[0m
\033[34mEnter the option's number here: \033[0m""")

if choise == "1":
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(int(passwordrange)))
    print("The Password is: " + password)   
elif choise == "2":
    alphabet2 = string.ascii_letters + string.digits
    password2 = ''.join(secrets.choice(alphabet2) for i in range(int(passwordrange)))
    print("The Password is: " + password2)
elif choise == "3":
    alphabet3 = string.ascii_lowercase + string.ascii_uppercase
    password3 = ''.join(secrets.choice(alphabet3) for i in range(int(passwordrange)))
    print("The Password is: " + password3)
elif choise == "4":
    alphabet4 = string.ascii_uppercase
    password4 = ''.join(secrets.choice(alphabet4) for i in range(int(passwordrange)))
    print("The Password is: " + password4)
elif choise == "5":
    alphabet5 = string.ascii_lowercase
    password5 = ''.join(secrets.choice(alphabet5) for i in range(int(passwordrange)))
    print("The Password is: " + password5)
else:
    print("\033[31mYou Entered an Unavailable option. Please try again.\033[0m")
    exit()
