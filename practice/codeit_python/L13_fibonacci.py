def fibonacci():
    current = 1
    next = 1
    count = 2

    while count < 50:
        temp = current
        current = next
        next = temp + current
        count += 1
    return current
    
print(fibonacci())
