stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    totalInv = 0
    print('Inventory')
    for key, value in inventory.items():
        print(value, key)
        totalInv += value
    print('Total number of items:', totalInv)
    
displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        item_num = inventory.get(item, 0)
        inventory[item] = item_num + 1
    return inventory

inv = {'gold coin':42, 'rope':1}
inv = addToInventory(inv, dragonLoot)
print()
displayInventory(inv)