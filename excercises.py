list = ['1', '2', '3', '4', '5']
for i in range(1,6):
    print("Add a new item to the list")
    list[i-1] = input()
    print ("New element: ", list[i-1])
pets = ('Manchitas', 'Fiona', 'Betoben', 'Morgan', 'Luno', 'Solo', 'Mimbi')
j = 1
while j<8:
    print(pets[j-1])
    j=j+1
verbs = {"Jump":"Saltar", "Run":"Correr", "Walk":"Volar"}
print (verbs)
print("Write the correct verb in spanish for 'Walk'")
verbs['Walk']= input()
print (verbs)