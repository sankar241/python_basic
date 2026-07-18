go = (1, 'java', [3, 4], ("python", 78))

print(type(go))
print(go.index('java'))
print(go[2][1])
print(go.count('python'))
print(go.count(("python", 78)))

list_ = (1, 2, 3, 4, 5, "hello", 3.14, True, [1, 2, [11, "world"], 3])

print(type(list_))
print(list_[0])
man = {
    1: 9,
    "name": "sankar",
    (1, 2): 5
}

print(man)
details = {
    "name": "sankar",
    "college": "simh",
    "pan": 546446,
    "adhr": 6876,
    "pin": 1234
}

print(details.keys())
print(details.values())
print(details.items())

details.update({"name": "bhavani sankar"})
details.update({"gender": "male"})
print(details)

details["name"] = "bhavani sankar"
print(details)
print(details["name"])
