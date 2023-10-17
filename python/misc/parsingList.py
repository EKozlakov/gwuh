names = "gene;boris;isaac;ulysses;jerry;claudia"
print(names)
List = names.split(";", 7) #if specified num > num of elements, will parse out all elements.
print(List)