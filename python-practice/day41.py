# Question: Day 41: Create a custom exception class for validating age (must be 18+).
class UnderageError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is below minimum required 18 years")

def validate_age(age):
    if age < 18:
        raise UnderageError(age)
    print("Age validation successful")

try:
    validate_age(20)  # Valid
    validate_age(15)  # Raises UnderageError
except UnderageError as e:
    print(e)
