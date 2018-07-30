def fake_bin(x):

    result = ""
    for i in x:

        if i < "5":
            result += "0"

        else:
            result += "1"

    return result




print fake_bin("12345678591")
print fake_bin("45385593107843568")
print fake_bin("55555555")
print fake_bin("453855")
print fake_bin("93137")
