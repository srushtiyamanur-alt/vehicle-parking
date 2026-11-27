rates = {
    "two wheeler": 20,
    "four wheeler": 50,
    "heavy vehicle": 100
}

vtype = input("Vehicle type (two wheeler/four wheeler/heavy vehicle): ").lower()
hours = int(input("Enter parking duration in hours: "))
vno = input("Enter vehicle number: ")
fee = rates[vtype] * hours

print("Vehicle type:", vtype)
print("Duration:", hours, "hours")
print("Vehicle number:", vno)
print("Total fee: Rs", fee)