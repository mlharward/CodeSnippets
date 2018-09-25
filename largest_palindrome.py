def palindrome():
    """This is a simple function to find the largest palindrome
    that is a product of two three digit numbers."""
    i = 1
    j = 1
    highest = 0
    test = 0
    while i < 1000:
        while j < 1000:
            test = i * j
            check = str(test)
            if(check == check[::-1]):  #checks if palindrome
                if(test > highest):    #checks if higher than prev.
                    highest = test
            j += 1
        i += 1
        j = 1
    return highest
