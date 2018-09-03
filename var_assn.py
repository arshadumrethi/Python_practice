
#Function that converts DNA code to RNA by replacing T with U
def DNAtoRNA(dna):
    result = ""
    for i in dna:
        if i == "T":
            result += "U"
        else:
            result += i

    return result

print DNAtoRNA("TTTT")
print DNAtoRNA("GCAT")
