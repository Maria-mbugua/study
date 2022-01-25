#jane is to pay 50 ksh
#anything above 50 split to 100s and 50s


var_parking_amount=50
print("Your parking is KES: "+ str(var_parking_amount))

#input payment note
var_note = int(input('Please enter your NOTE: '))

#obtain change
var_balance= var_note-var_parking_amount

#get the number of full hundreds
var_divisor = var_balance//100

#we do a modulus to get the remainder and calculate coins and fiftys
var_modulus=var_balance%100

#Print total change
print ("Your change is : " + str(var_balance))

#print the hundreds change
print("You will receive "+ str(var_divisor)+ " Notes of KES 100")
#print the coins and fiftys change
print("You will receive 1 notes of KES: "+ str(var_modulus)) 