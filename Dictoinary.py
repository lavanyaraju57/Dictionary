# book={
#     1:"Python Programming",
#     2:"Core Python programming",
#     3:"Advance Python Programming"
# }
# print(book[2])
# print(book[1])

"""DICTIONARY METHODS"""

'''KEYS , VALUES , ITEMS'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}

# print(h[1],type(h[1]))
# print(h[2],type(h[2]))
# print(h,type(h))
# print(h.keys())
# print(h.values())
# print(h.items())

'''CLEAR'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}
# h.clear()
# print(h)

'''FROMKEYS'''

# a=[101,102,103,104,105,'hd']
# b=dict.fromkeys(a)
# print(b,type(b))
# print(dict.fromkeys(a,'python'))
# print(dict.fromkeys(b,'world'))

'''GET'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}

# print(h.get(2))
# print(h[2])

'''POP'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}

# h.pop(4)
# print(h)

'''POPITEM'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}

# h.popitem()
# print(h)

'''UPDATE'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}

# h.update({8:'Core Python'})
# print(h)
# h.update({9:'Adv Python'})
# print(h)

'''SETDEFAULT'''

# h={1:"", 2:"python", 3:7, 4:6.2,
# 5:[1,4], 6:(4,3), 7:{1,2}, 8:{3:"world"}}

# h.setdefault(8,'devOps')
# h.setdefault(10,'devOps')
# print(h)




