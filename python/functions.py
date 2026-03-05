def movie_tickets(price,quantity):
    total=price*quantity
    print(f"total ammount is{total}")
    if total>=2000:
        print("coke+popcorn")
    elif total>=1500 and total<2000:
        print("coke")
    else:
        print("thank you")
movie_tickets(int(input("enter price of tickets: ")),(int(input("enter the qantity: "))))