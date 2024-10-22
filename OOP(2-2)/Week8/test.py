result = '''==========Part 1==========
[Constructor] Constructing VendingMachine
[Constructor] Constructing State: No Coin
[Constructor] Constructing State: Has Coin
[Constructor] Constructing State: Sold Out
Action: Initialization | Current State: No Coin | Coin Value: 0
[Constructor] Product created: Cola (ID: 1, Price: $1.5)
[Constructor] Product created: Chips (ID: 2, Price: $1)
[Constructor] Product created: Water (ID: 3, Price: $1)
==========Part 2==========
Current Inventory:
Product: Cola (ID: 1, Price: $1.5)
Product: Chips (ID: 2, Price: $1)
Product: Water (ID: 3, Price: $1)
Total items: 3
==========Part 3==========
Action: State Changed | Current State: Has Coin | Coin Value: 1
Action: Insert Coin | Current State: Has Coin | Coin Value: 1
Action: Insert Coin | Current State: Has Coin | Coin Value: 1.5
Action: State Changed | Current State: No Coin | Coin Value: 0
[Destructor] Product destroyed: Cola (ID: 1)
Action: Dispense | Current State: No Coin | Coin Value: 0
==========Part 4==========
Action: State Changed | Current State: Has Coin | Coin Value: 1
Action: Insert Coin | Current State: Has Coin | Coin Value: 1
Action: State Changed | Current State: No Coin | Coin Value: 0
[Destructor] Product destroyed: Water (ID: 3)
Action: Dispense | Current State: No Coin | Coin Value: 0
==========Part 5==========
Action: State Changed | Current State: Has Coin | Coin Value: 0.5
Action: Insert Coin | Current State: Has Coin | Coin Value: 0.5
Insufficient funds. Please insert more coins.
Current balance: $0.5, Required: $1
Action: Dispense | Current State: Has Coin | Coin Value: 0.5
Action: Insert Coin | Current State: Has Coin | Coin Value: 1
Action: State Changed | Current State: Sold Out | Coin Value: 0
[Destructor] Product destroyed: Chips (ID: 2)
Action: Dispense | Current State: Sold Out | Coin Value: 0
==========Part 6==========
SOLD OUT: No additional coin accepted
Action: Insert Coin | Current State: Sold Out | Coin Value: 0
No product to dispense
Action: Dispense | Current State: Sold Out | Coin Value: 0
Current Inventory:
Total items: 0
==========Part 7==========
[Constructor] Product created: Chocolate (ID: 4, Price: $1.25)
[Constructor] Product created: Orange Juice (ID: 5, Price: $1.75)
Action: State Changed | Current State: No Coin | Coin Value: 0
Current Inventory:
Product: Chocolate (ID: 4, Price: $1.25)
Product: Orange Juice (ID: 5, Price: $1.75)
Total items: 2
==========Part 8==========
Action: State Changed | Current State: Has Coin | Coin Value: 2
Action: Insert Coin | Current State: Has Coin | Coin Value: 2
Change returned: $0.75
Action: State Changed | Current State: No Coin | Coin Value: 0
[Destructor] Product destroyed: Chocolate (ID: 4)
Action: Dispense | Current State: No Coin | Coin Value: 0
Action: State Changed | Current State: Has Coin | Coin Value: 2
Action: Insert Coin | Current State: Has Coin | Coin Value: 2
Change returned: $0.25
Action: State Changed | Current State: Sold Out | Coin Value: 0
[Destructor] Product destroyed: Orange Juice (ID: 5)
Action: Dispense | Current State: Sold Out | Coin Value: 0
Current Inventory:
Total items: 0
[Destructor] Destructing VendingMachine
[Destructor] Destructing State: No Coin
[Destructor] Destructing State: Has Coin
[Destructor] Destructing State: Sold Out'''

result = result.split('\n')
size = len(result)
count = 0
for i in result:
    text = input()
    if i == text:
        print("Correct")
        count += 1
    else:
        print("Incorrect")
        print(f"Expected: {i}, Got: {text}.")

print(f"Score: {count}/{size}")