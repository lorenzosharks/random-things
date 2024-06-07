hour=int(input("Hour: "))

minute=float(input("Minute: "))

ahour=0

if hour==12:
    ahour=0
else:
    ahour=hour

a=ahour
b=minute

if 5*a>b:
    result=(30*a)+(b/2)-(6*b)
else:
    result=(6*b)-(30*a)-(b/2)

if result<0:
    result=result*(-1)

oresult=360-result

if oresult>result:
    oresult=result
    result=360-oresult
else:
    oresult=oresult
    result=result

print("Small angle: " + str(oresult))
print("Large angle: " + str(result))