# Question: Day 38: Create a closure that remembers and updates a counter value.
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter()
print(counter1())  # 1
print(counter1())  # 2
