"""
week2 MiT with EDX - Python programming
Bisection search example


"""

def biSecSquare(x=25, epsilon = 0.01):
    """
    somewhere over the rainbow
    """
    # x = 25
    # epsilon = 0.01
    numGuesses = 0

    low = 0.0
    high = x
    ans = (high + low) / 2.0

    print('low    <   answer   <  high')
    while abs(ans**2 - x) >= epsilon :
        print('  {}  <  {}  < {} '.format(low, ans, high))
        numGuesses += 1

        if ans**2 < x :
            low = ans
        else:
            high = ans
        
        ans = (high + low) / 2.0

    print('  {}  <  {}  <  {} '.format(low, ans, high))
    print('Number of guesses (numGuesses) = {}.'.format(numGuesses))
    return('{} is close to square root of {}'.format(ans, x))
    
