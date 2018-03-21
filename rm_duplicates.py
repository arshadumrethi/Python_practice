#Write a function remove_duplicates that takes in a list
#and removes elements of the list that are the same.

def remove_duplicates(x):
    new =[]
    for i in x:
        if i not in new:
            new.append(i)
    return new

print remove_duplicates([1,1,2,2])
