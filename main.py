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
    if x == "Emperor penguin":
        return "Near Threatened"
    if x =="King penguin":
        return "Least Concern"
    if x == "Little penguin":
        return "Least Concern"
    if x == "Southern rockhopper penguin":
        return "Vulnerable"
    if x == "Macaroni penguin":
        return "Vulnerable"
    if x == "Nothern rockhopper penguin":
        return "Endangered"
    if x == "Fiordland penguin":
        return "Vulnerable"
    if x == "Snares penguin":
        return "Vulnerable"
    if x == "Royal penguin":
        return "Near Threatened"
    if x == "Erect-creasted penguin":
        return "Endangered"
    if x == "Yellow-eyed penguin":
        return "Endangered"
    if x == "Adelie penguin":
        return "Least Concern"
    if x == "Chinstrap penguin":
        return "Least concern"
    if x == "Gentoo penguin":
        return "Least concern"
    if x == "African penguin":
        return "Endangered"
    if x == "Humboldt penguin":
        return "Vulnerable"
    if x == "Magellanic penguin":
        return "Near Threatened"
    if x == "Galapagos penguin":
        return "Endangered"

print(penguin("African penguin"))