# defining list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

print(myFruitList[-3])
print(myFruitList[-2])
print(myFruitList[-1])

myFruitList[2] = "orange"
print(myFruitList)

# defining tuple -- nilai tuple gabisa diganti spt pada list yg mutable
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# list lebih besar daripada tuple
import sys
 
myFruitList = ["apple", "banana", "cherry"]
myFinalAnswerTuple = ("apple", "banana", "pineapple")
 
print(f"Size of integer {myFruitList}: {sys.getsizeof(myFruitList)} bytes")
print(f"Size of integer {myFinalAnswerTuple}: {sys.getsizeof(myFinalAnswerTuple)} bytes")

# defining dict
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

