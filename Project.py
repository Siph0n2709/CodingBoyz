# Agnivesh and Parth's Convenience Store # 

print("Welcome to Ikpran's and Pranik's convenience store.")
ItemsBought = []
ItemsPrice = 0
def StoreFunc():
    global ItemsBought
    global ItemsPrice
    Items = {'Item 1': 17.99, 'Item 2': 18.99}
    x = str(input("What Would You Like To Buy? "))
    if x in Items:
        ItemsBought.append(x)
        ItemsPrice += Items[x]
        print(x + ' is $' + str(Items[x]))
        

    again = str(input('Would You Like to Buy more items? (yes/no) ')).lower()
    if again == 'yes':
        StoreFunc()
    else:
        for item in ItemsBought:
            print(str(item) + '                       ' + str(Items[item]))

StoreFunc()
print('Total: ' + str(ItemsPrice))
print("Have a good day")