inch = int(input("Enter the measurement in incles: "))
# 1 inch = 2.54 cm 
def inch_to_cm_convertor():
    cm = inch * 2.54
    return cm 

print(f"{inch_to_cm_convertor()}cm") 