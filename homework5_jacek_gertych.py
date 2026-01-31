## list exercise

antipsychotics = ['aripriprazole', 'chlorpromazine', 'clozapine', 'fluphenazine', 'haloperidol', 'prochlorperazine']

print("The first two items in the list are: ",', '.join(antipsychotics[:2]))
print("The middle two items in the list are: ",', '.join(antipsychotics[2:4]))
print("The first and last items in the list are: ",', '.join(antipsychotics[0:6:5]))

print("\n")
## tuple exercise

italianfoods = ('cheese tortellini', 'fettucine alfredo', 'pepperoni pizza', 'salmon risotto', 'spaghetti bolognese')
print("Our menu: ")
for i in italianfoods:
    print(i)

italianfoodslist = list(italianfoods)
italianfoodslist[0] = 'beef lasagna'
italianfoodslist[1] = 'caponata'
newitalianfoods = tuple(italianfoodslist)

print("\n")

print("Our new menu: ")
for i in newitalianfoods:
    print(i)
