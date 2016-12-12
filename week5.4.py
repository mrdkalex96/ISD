magnitude = float(input("Please insert the magnitude of the earthquake "))
if magnitude >=8.0:
    print("Most structure fall")
elif magnitude >=7.0:
    print("Many building destroyed")
elif magnitude >=6.0:
    print("Many buildings considerably damaged, some of them collapsed")
elif magnitude >=4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")
