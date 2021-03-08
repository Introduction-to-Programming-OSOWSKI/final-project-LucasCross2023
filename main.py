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
    if x == "emperor penguin":
        return "near threatened"
    if x =="king penguin":
        return "least concern"
    if x == "little penguin":
        return "least concern"
    if x == "southern rockhopper penguin":
        return "vulnerable"
    if x == "macaroni penguin":
        return "vulnerable"
    if x == "nothern rockhopper penguin":
        return "endangered"
    if x == "fiordland penguin":
        return "vulnerable"
    if x == "snares penguin":
        return "vulnerable"
    if x == "royal penguin":
        return "near threatened"
    if x == "erect-creasted penguin":
        return "endangered"
    if x == "yellow-eyed penguin":
        return "endangered"
    if x == "adelie penguin":
        return "least concern"
    if x == "chinstrap penguin":
        return "least concern"
    if x == "gentoo penguin":
        return "least concern"
    if x == "african penguin":
        return "endangered"
    if x == "humboldt penguin":
        return "vulnerable"

    if x == "galapagos penguin":
        return "endangered"

print(penguin("african penguin"))