print("Welcome to our Theme Park !!!")

name = input("May i ask your name? ")

print("Hello " + name + " we Hope your having a good day!")

height = int(input("May i ask your height? "))
unit = input("Was this in (I)nches or (F)eet? ")

if unit.upper() == "F":
    converted = height * 12 - 36
    if converted >= 10:
        print("Congradulations your tall enoff to ride all the rides!")
    elif converted >= 0:
        print("You may only ride in the kids section.")
    elif converted < 0:
        print("Sorry your not tall enoff yet mabey next time we still hope you enjoy your time here.")



elif unit.upper() == "I":
    base = height - 36
    if base >= 10:
        print("Congradulations your tall enoff to ride all the rides!")
    elif base >= 0:
        print("You may only ride in the kids section.")
    elif base < 0:
        print("Sorry your not tall enoff yet mabey next time we still hope you enjoy your time here.")


days = input("How many days will you be staying with us? ")

cost = int(days) * 40
print("So you will be staying " + days + " days with us thats fantastic!")
print("that will be " + str(cost) + " dollars please.")
print("Please enjoy your stay " + name)

