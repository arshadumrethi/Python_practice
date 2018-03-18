
##This script takes in a sequence and determines what kind of credit card it belongs to.
#Amex cards begin with 34 or 37 and contain 15 digits
#Discover cards begin with 6011, 16 digits
#Mastercard begins with 51/52/53/54/55, 16 digits
#Visa begins with 4, 13 or 16 digits

def get_issuer(number):
    card = str(number)
    nums = len(card)

    if card[:2] in ("34", "37") and nums == 15:
        return "AMEX"
    elif card[:4] == "6011" and nums == 16:
        return "Discover"
    elif 51 <= int(card[:2]) <= 55 and nums == 16:
        return "Mastercard"
    elif card[0] == "4" and nums in (13, 16):
        return "VISA"
    return "Unknown"

get_issuer(4111111111111111)

#First attempt didnt pass all test cases.
# def get_issuer(number):
#     string_num = str(number)
#     if len(string_num) == 15:
#         print "AMEX"
#
#     elif string_num[:4] == 6011:
#         print "Discover"
#
#     elif string_num[:2] in range(50, 56):
#         print "Mastercard"
#
#     elif string_num[0] == 4: #and len(string_num) == 16:
#         print "VISA"
