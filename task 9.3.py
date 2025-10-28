# Problem 9.3: Custom Exception for Age Validation

class InvalidAgeException(Exception):
    """Custom Exception for invalid voting age."""
    pass


def check_voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise InvalidAgeException("❌ You must be at least 18 years old to vote.")
        else:
            print("✅ You are eligible to vote!")
    except InvalidAgeException as e:
        print(e)
    except ValueError:
        print("❌ Error: Please enter a valid integer age.")
    finally:
        print("✅ Age verification process completed.\n")

# Run the function
check_voting_eligibility()
