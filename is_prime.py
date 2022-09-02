def is_prime(n):
    # if neg, 0, 1 will return false
    if n < 2: 
        return False 
        
    # tests all numbers between 2 and n if factor
    for d in range(2,(n//2 + 1)):
        if n%d == 0:
            return False
    return True


if __name__ == "__main__": 
    while True:
        n = int(input("> "))
        if is_prime(n) == True:
            print("True")
        else:
            print("False")