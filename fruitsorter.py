fruit = (input("What kind of fruit am i sorting?     "))
fruit = fruit.capitalize()
if fruit == 'Apple':
    print ("Apples in bin 1")
elif fruit == 'Orange':
    print ("Oranges in bin 2")
elif fruit == 'Banana':
    print ("Bananas in bin 3")
else:
    print ("Error! I do not recognize this fruit!")
