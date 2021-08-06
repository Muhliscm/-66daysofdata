
temp = float(input("Enter temperature\n"))

print("Choose unit c or  f")
unit = input("Enter unit\n")

if unit == "c" or unit == "C":
    converted = (temp * 9/5) + 32
    print("Temperature in farenhet : ", converted)
elif unit == "F" or unit == "f":
    converted = (temp - 32) * (5/9)
    print("Temperature in degree celcious : ", converted)
else:
    print("unknown unit")