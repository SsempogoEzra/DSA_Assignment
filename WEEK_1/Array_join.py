# Write a python program that accepts a group of N domestic animals and a group of X wild animals. 
# Your program should print N + X animals after entering each group.
# The groups should be organised into arrays and later the arrays are combined and  printed.

def get_animal_group(group_name):
    num_animals = int(input(f"Enter the number of {group_name} animals: "))
    animal_group = []
    
    for i in range(num_animals):
        animal_name = input(f"Enter {group_name} animal {i+1} name: ")
        animal_group.append(animal_name)
    
    return animal_group

def print_animal_group(group_name, animal_group):
    print(f"\n{group_name} Animals u entered:")
    print(animal_group)


domestic_animals = get_animal_group("Domestic")
wild_animals = get_animal_group("Wild")


print_animal_group("Domestic", domestic_animals)
print_animal_group("Wild", wild_animals)

all_animals = domestic_animals + wild_animals

print("\nAll Animals together:")
print(all_animals)