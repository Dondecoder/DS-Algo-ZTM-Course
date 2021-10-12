def compressBoxesTwice (boxes, boxes2):
    boxes.forEach((boxes))
    print (boxes)

    boxes2.forEach(boxes2)
    print(boxes2)

# The run time of this would be O(a +b). The reason being that there are two different paramaters so you can't say O(n + n) because they
# are not the same. If they were you could. If the for loop was nested inside the other for loop the equation would be O(a *b). Rule of 
# thumb is if the loops are nested then they should be multiplied if they aren't then you can add the variables. 