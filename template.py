"""Password Strength Audit.

Asks the user how many passwords to check, rates each one as Strong,
Moderate, or Weak, and prints a summary of the totals at the end.
"""


# Asks the user for a count and keeps asking until the answer is valid.
def get_password_count():
    """Prompt until the user enters a positive whole number; return that number."""
    while True:
        try:
            num = int(input("Enter the number of passwords to audit: "))
            if num > 0:
                return num
            print("Invalid number, please try again")
        except ValueError:
            # int() raises ValueError when the user types letters instead of digits.
            print("Invalid number, please try again")


# Looks at one password and decides how strong it is.
def evaluate_password(password):
    """Return Strong, Moderate, or Weak after examining one password."""
    # Local variables that track what we have found so far.
    # They start False and flip to True as soon as we see that character type.
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Loop through the password one character at a time.
    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            # Anything that is not a letter or a digit counts as special.
            has_special = True

    # Count how many of the four character-type requirements were met.
    types_met = 0
    if has_upper:
        types_met = types_met + 1
    if has_lower:
        types_met = types_met + 1
    if has_digit:
        types_met = types_met + 1
    if has_special:
        types_met = types_met + 1

    # Apply the rating rules, strictest first.
    if len(password) >= 12 and types_met == 4:
        return "Strong"
    elif len(password) >= 8 and types_met >= 3:
        return "Moderate"
    else:
        return "Weak"


# Prints the final totals that main() collected.
def display_summary(strong_count, moderate_count, weak_count):
    """Display the totals for each password-rating category."""
    print()
    print("--- Password Audit Summary ---")
    print("Strong passwords:  ", strong_count)
    print("Moderate passwords:", moderate_count)
    print("Weak passwords:    ", weak_count)


# Runs the program by calling the other three functions.
def main():
    """Coordinate the password audit."""
    # Local counters, one for each rating.
    strong_count = 0
    moderate_count = 0
    weak_count = 0

    # Ask how many passwords to check. That function does the validating.
    count = get_password_count()

    # Repeat once for each password the user asked for.
    for number in range(1, count + 1):
        password = input("\nPassword " + str(number) + ": ")

        # Send the password out as a parameter, get the rating back.
        rating = evaluate_password(password)
        print("Rating:", rating)

        # Add one to whichever counter matches the rating.
        if rating == "Strong":
            strong_count = strong_count + 1
        elif rating == "Moderate":
            moderate_count = moderate_count + 1
        else:
            weak_count = weak_count + 1

    # After the loop, pass the three totals to the summary function.
    display_summary(strong_count, moderate_count, weak_count)


if __name__ == "__main__":
    main()
