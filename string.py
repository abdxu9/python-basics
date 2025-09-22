print(type("Hello, World"))
string1 = "Hello, World"
print(len(string1))

string2 = "This planet has—or rather had—a problem, which was this: most of the people living on it were unhappy for pretty much of the time. Many solutions were suggested for this problem, but most of these were largely concerned with the movements of small green pieces of paper, which is odd because on the whole it wasn’t the small green pieces of paper that were unhappy. —Douglas Adams, TheHitchhiker’s Guide to the Galaxy"
print(len(string2))

string3 = """This planet has—or rather had—a problem, which was
 this: most of the people living on it were unhappy for
 pretty much of the time. Many solutions were suggested
 for this problem, but most of these were largely con
cerned with the movements of small green pieces of
 paper, which is odd because on the whole it wasn’t the
 small green pieces of paper that were unhappy.
 —Douglas Adams, TheHitchhiker’s Guide to the Galaxy"""
print(len(string3))

print(string2)
print("\n")
print(string3)

print("He said: \"Hello everyone\" ")
print("In french \"the man\" is translated as \"l\'homme\"")

string1 = "Hello"
string2 = "World"
string3 = string1 + " " + string2 
print(string3)

print(string1[0])
print(string2[0:3])

print(string3.lower())
print(string3.upper())

string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honey Badger"

print("\n")
print(string1.lower())
print("\n")
print(string2.lower())
print("\n")
print(string3.lower())
print("\n")
print(string4.lower())

print("\n")
print(string1.upper())
print(string2.upper())
print("\n")
print(string3.upper())
print("\n")
print(string4.upper())
print("\n")

string1 = "    Filet Migon"
string2 = "Brisket    "
string3 = "    Cheeseburger   "

print(string1.lstrip()) 
print(string2.rstrip())
print(string3.strip())

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"

print(string1.startswith("be"))  # False 
print(string2.startswith("be"))  # True
print(string3.startswith("be"))  # False
print(string4.startswith("be"))  # False

print(string1.lower().startswith("be"))
print(string3.lower().startswith("be"))
print(string4.lower().lstrip().startswith("be"))
      