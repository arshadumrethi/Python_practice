def deleteReoccurringCharacters(string):
    outputString = ''
    for char in string:
        if char not in outputString:
            outputString += char
    return outputString

print deleteReoccurringCharacters("aabbcc")
