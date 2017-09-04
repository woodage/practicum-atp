def function_to_doctest(a):
    """
    Deze functie neemt een reeks van getallen en sorteert deze in oplopende volgorde (insertion sort methode).
    @param a de lijst om te sorteren
    @return de gesorteerde variant van a
    #TODO Insert DocTest
    
    >>> function_to_doctest([3, 6, 4, 5, 5])
    [3, 4, 5, 5, 6]
    """
    for p in range(1,len(a)):
        j = p
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j = j - 1
    return a

doctest.testmod()