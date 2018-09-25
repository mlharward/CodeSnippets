def pig_latin(you):
    """Turns any word you run thorugh it into pig latin.
    One of the first programs I wrote, not advanced code.
    """
    vowels = ('a','e','i','o','u','y','A','E','I','O','U','Y')
    if(you.startswith(vowels)):
        you = you + "hay"
    else:
        you = you[1:] + you[0] + "ay"
    return you
