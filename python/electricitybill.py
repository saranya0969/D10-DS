units=int(input('enter no of units consumed: '))
bill=0
if units<=100:
    bill=units*2
    print(f"total electricity bill={bill}")
elif units<=200:
    bill=(100*2)+(units-100)*3
    print(f"total electricity bill={bill}")
else:
    bill=(100*2)+(units-200)*5
    print(f"total electricity bill={bill}")