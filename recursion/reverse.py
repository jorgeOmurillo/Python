def reverseMe(text):

    if text == "":
        return text

    else:
        return text[len(text)-1] + reverseMe(text[:len(text)-1])

print reverseMe("prueba")
