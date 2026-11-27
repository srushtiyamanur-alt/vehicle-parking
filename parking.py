rates = {
    "two wheeler": 20,
    "four wheeler": 50,
    "heavy vehicle": 100
}

vtype = input("Vehicle type (two wheeler/four wheeler/heavy vehicle): ").lower()
hours = int(input("Enter parking duration in hours: "))

fee = rates[vtype] * hours

print("Vehicle type:", vtype)
print("Duration:", hours, "hours")
print("Total fee: Rs", fee)