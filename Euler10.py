if True:
    target = 2000000
    
    from Primes import primes_below
    answer = sum(primes_below(target))
    print(answer)
    raw_input("Press ENTER")
