from datetime import datetime
fruit_calories = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Grapefruit": 60,
    "Grapes": 90,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
    "Cantaloupe": 50,
    "Honeydew Melon": 50
}
fruit_prices = {
    "Apple": 15,
    "Avocado": 25,
    "Banana": 10,
    "Grapefruit": 20,
    "Grapes": 30,
    "Kiwifruit": 35,
    "Lemon": 5,
    "Lime": 5,
    "Nectarine": 20,
    "Orange": 12,
    "Peach": 15,
    "Pear": 18,
    "Pineapple": 25,
    "Plums": 15,
    "Strawberries": 40,
    "Sweet Cherries": 50,
    "Tangerine": 10,
    "Watermelon": 20,
    "Cantaloupe": 20,
    "Honeydew Melon": 22
}

itemlist={}
totalcalories=0
totalprice=0
print("Welcome to Fruitopia: A paradise of fresh and exotic fruits!")
while True:
    item=input("Item (type 'exit' to finish): ").lower().title().strip()
    if item in fruit_calories:
        print("Calories:",fruit_calories[item])
    if item in fruit_prices:
        print(f"Price: ₹{fruit_prices[item]}")
        while True:
            yorn = input("Do you want to buy the fruit? (yes/no): ").lower().strip()
            if yorn in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")
        if yorn=="yes":
            while True:
                try:
                    portions=int(input("How many portions? "))
                    if portions<=0:
                         print("Please enter a positive number.")
                         continue
                    if item in itemlist:
                        itemlist[item]+=portions
                    else:
                        itemlist[item]=portions
                    totalcalories += fruit_calories[item] * portions
                    totalprice+=fruit_prices[item]*portions
                except ValueError:
                    print("Please enter a valid number not in words.")
                else:
                    break

        
            
    elif item.lower()=="exit":
                if not itemlist:
                     print("Nothing purchased.")
                print("\nYou bought:")
                
                for item in sorted(itemlist):
                    print(f"{item} - {itemlist[item]} portions")
                print("\nTotal calories:",totalcalories)
                print(f"Fruits price before Tax(GST): ₹{totalprice}\nGST:5%\nTotal price after tax:{totalprice*(105/100)}")

                break
        
    else:
        print(f"Sorry, we don't have that fruit.\nTry: {', '.join(sorted(fruit_calories.keys()))}")
        continue
if itemlist:
    customername=input("Thank you for shopping! Please enter your name for the receipt: ").lower().title()
    timeNow=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("fruits.csv","a", encoding="utf-8") as file:
        file.write(f"Customer Name: {customername}\n")
        file.write(f"Time: {timeNow}\n")
        file.write("Purchase Summary:\n")
        for item in sorted(itemlist):
            file.write(f"\n{item}-{itemlist[item]} portions")
        file.write(f"\n")
        file.write(f"\nTotal price: ₹{totalprice*(105/100)}")
        file.write(f"\nTotal Calories: {totalcalories}\n---------------\n")