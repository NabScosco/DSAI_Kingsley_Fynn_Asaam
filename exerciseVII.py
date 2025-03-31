def human_to_dog_years(human_years):
    if human_years < 0:
        return "Error: Age cannot be negative."
    elif human_years <= 2:
        return human_years * 10.5
    else:
        return (2 * 10.5) + ((human_years - 2) * 4)

try:
    human_years = float(input("Enter human years: "))
    dog_years = human_to_dog_years(human_years)
    print(f"Equivalent dog years: {dog_years}")
except ValueError:
    print("Error: Please enter a valid number.")