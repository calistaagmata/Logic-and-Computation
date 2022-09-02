from is_prime import is_prime

def nth_prime(n):
    # create a list of known prime numbers 
    known_primes = [] 
    # count variable to know distance from n
    count = 0 
    # test variable is the number testing 
    test = 1 
    # if the nth prime number is in list check list \
    if n <= len(known_primes):
        return known_primes[n]
    else:
    # if not in list test all numbers is prime until reach n 
        while count != n: 
            test += 1 
            if is_prime(test) == True:
                known_primes.append(count) 
                count += 1 
    return test
    
             
if __name__ == "__main__":
    while True: 
        n = int(input("> "))
        print(nth_prime(n))