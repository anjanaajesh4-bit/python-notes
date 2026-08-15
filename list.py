def countdown(n):
    print(n)
    if n > 1:
        countdown(n-1)
countdown(10)