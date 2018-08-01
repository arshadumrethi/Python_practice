def quote(fighter):
    s = fighter
    s = s.upper()


    if "GEORGE" in s:
        return "I am not impressed by your performance."

    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"


print quote('george saint pierre')
print quote('conor mcgregor')
print quote('George Saint Pierre')
print quote('Conor McGregor')
