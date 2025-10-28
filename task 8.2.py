# Problem 8.2: Message Formatting using Decorators

def uppercase_decorator(func):
    """Decorator to convert message to uppercase"""
    def wrapper():
        message = func()
        return message.upper()
    return wrapper


def lowercase_decorator(func):
    """Decorator to convert message to lowercase"""
    def wrapper():
        message = func()
        return message.lower()
    return wrapper


# --- Example Functions Using Decorators ---

@uppercase_decorator
def emphasize_message():
    return "This is an important announcement!"

@lowercase_decorator
def soft_message():
    return "PLEASE KEEP THE NOISE DOWN."


# --- Example Usage ---
print("\n📢 Formatted Messages:")
print("Uppercase Message:", emphasize_message())
print("Lowercase Message:", soft_message())
