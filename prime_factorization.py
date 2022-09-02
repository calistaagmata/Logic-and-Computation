def prime_factorization(n):
    # creates a list of facotrs 
    # d is the test number set to 2 
    factors = [] 
    d = 2
    
    # n + 1 to accommodate for 2 
    while d < (n + 1): 
        # checks if d is a factor of n 2
        # if a factor added to list, change n, reset d 
        if n % d == 0: 
            factors.append(d)
            n = n//d 
            d = 2
        # if not a factor test new d 
        else:
            d = d + 1
    return factors
          
if __name__ == "__main__":
    while True:   
        n = int(input("> "))
        print(prime_factorization(n))

