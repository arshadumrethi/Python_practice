a = "code"
b = "wa.rs"
name = a + b

print name

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
