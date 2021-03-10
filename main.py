def times10(x):
    return x * 10
print(times10(3))

def firstA(x):
    word = x
    if x[0] == "a":
        return True
    else:
        return False

print(firstA("aye"))

def sizer(x):
    if x <= 10:
        return "small"
    if 10 > x < 100:
        return "medium" 
    if x > 100:
        return "large"

print(sizer(1))

def doubleWord(x):
    return x + x

print(doubleWord("word"))

def penguin(x):
    for i in range(len(penguins)):
        if x == penguins[i]:
            return threat[i] 
    
penguins = ["king","macaroni","royal","african"]
threat = ["increasing", "vulnerable", "near threatened", "endangered"]

print(penguin("royal"))