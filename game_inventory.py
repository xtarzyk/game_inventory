import csv

eq = {
    "Bow": 1,
    "Arrows": 20,
    "Sword": 1,
    "Shield": 1,
    "Sandwich": 2,
    "Cool Hat": 1
}




def display_inventory(inventory):
    print("=========================\n   ITEM NAME  |  COUNT\n=========================")
    for key, value in inventory.items():
        print(key.rjust(12), " : ", value)
    print("=========================")
    


def add_to_inventory(inventory, added_items):
    for item_to_add in added_items:
        
        if item_to_add in inventory:
            inventory[item_to_add] = inventory[item_to_add] + 1
        else:
            inventory[item_to_add] = 1
add_to_inventory(eq, ["Short Sword", "Hero Cloak", "Shield", "Shield"])


#display_inventory(eq)

# add_to_inventory(eq, ["taczki"])

# # display_inventory(eq)


def remove_from_inventory(inventory, removed_items):
    for item_to_remove in removed_items:

        if item_to_remove in inventory:
            inventory[item_to_remove] = inventory[item_to_remove] - 1
            if inventory[item_to_remove] == 0:
                del inventory[item_to_remove]
        
            
            
remove_from_inventory(eq, ["Sandwich", "Cool Hat", "Sandwich"])

# # display_inventory(eq)

empty = eq.items()
count_asc = sorted(eq.items(), key=lambda x: x[1], reverse=True)
count_desc = sorted(eq.items(), key=lambda x: x[1])

def print_table(inventory, order):
    print("=========================\n   ITEM NAME  |  COUNT\n=========================")
    # sort_orders = sorted(inventory.items(), key=lambda x: x[1], reverse=True)

    for i in order:
	    print(i[0].rjust(12)," : ", i[1])
    print("=========================")

print_table(eq, count_asc)





# def import_inventory():
#     with open('E:\Dev\Python\\2nd weekend\Homework2\game_inventory\csv\import_inventory.csv', 'r') as importing:
#         csv_dict_reader = csv.DictReader(importing)
    
#         for row in csv_dict_reader:
#             print(row)

# import_inventory()

# path = "E:\Dev\Python\second weekend\Homework2\game_inventory\csv\import_inventory.csv"
# file = open(path, newline='')
# reader = csv.reader(file)

# header = next(reader)
# data = []

# for row in reader:
    