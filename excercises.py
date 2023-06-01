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
def operation():
   result = 0
   firstNumber = int(input("Write the first number"))
   secondNumber = int(input("Write the second number"))
   operand = input("Write the operand")
   if operand == '+':
     result = firstNumber+secondNumber
     print("The result of the sum is: ", result)
   elif operand == '-':
     result = firstNumber-secondNumber
     print("The result of the subtraction is: ", result)
   elif operand == '*':
     result = firstNumber*secondNumber
     print("The result of the multiplication is: ", result)
   elif operand == '/':
     result = firstNumber/secondNumber
     print("The result of the division is: ", result)
   else:
     print("That is not a valid operand")
print("Do you want to do an aritmetic operation?(say yes please)")
if input() == 'yes':
   operation()
else:
   print("Ok we are done")