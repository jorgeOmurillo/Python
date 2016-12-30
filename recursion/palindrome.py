def reverseMe(text):

    if text == "":
        return text

    else:
        return text[len(text)-1] + reverseMe(text[:len(text)-1])


def isPal(newText):
    
    if newText == reverseMe(newText):
        return True
    else:
        return False

print isPal("ana")
