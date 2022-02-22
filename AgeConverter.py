

age = int(input("How old are you? (in years): "))
def ageConvert():
    type = input("What unit do you want to be covnerted to? (m/d/h/mi/s): ")
    if type == "m":
        print(age * 12)
    elif type == "d":
        print(age * 365)
    elif type == "h":
        print(age * 8760)
    elif type == "mi":
        print(age * 525600)
    elif type == "s":
        print(age * 3.154e+7)
    else:
        print("Please enter a valid unit type: ")
        ageConvert()
ageConvert()