
boxes = ['a','b','c','d','e']

def logAllPairsOfArray (array):
    for i in range(len(array)):
        for j in range (len(array)):
            print(array[i],array[j])

logAllPairsOfArray(boxes)

# When you see nested loops a good rule of thumb is to think multiplication. Nested loops usually mean multiplication.  