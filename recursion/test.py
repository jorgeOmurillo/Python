def testRecur(suma):

    print suma

    if suma == 5:
        return 0
    
    return suma + testRecur(suma+1)

print testRecur(1)
