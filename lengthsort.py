x = ["Telescopes", "Glasses", "Eyes", "Monocles"]
y = ["", "moderately", "brains", "pizza"]
z = ["i", "oo", "ppp", "kkkk", "mmmmm", "bbbbbb"]

def sort_by_length(arr):
    return sorted(arr, key=len)
    # arr.sort(key= lambda x:len(x))

# def sort_by_length(a):
#     n = len(a)
#     for i in range(n):
#         for j in range(i+1,n):
#             if len(a[i]) > len(a[j]):
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
#     return a

print sort_by_length(x)
print sort_by_length(y)
print sort_by_length(z)
