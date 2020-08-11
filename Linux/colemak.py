import os

print("Keyboard layout customizer, Aden@c MIT 2020\nThis script is meant for linux users, using this on windows or mac will not work.\n\n")

colemaken = input("What keyboard layout would you like to use:\n1. Dvorak\n2. Colemak\n3. Qwerty\nType in the number you would like execute (1, 2, 3): ")


if(colemaken == "1"):
    os.system("setxkbmap us -variant dvorak")
elif(colemaken == "2"):
    os.system("setxkbmap us -variant colemak")
elif(colemaken == "3"):
    os.system("setxkbmap us")
