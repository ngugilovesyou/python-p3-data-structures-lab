spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [names["name"] for names in spicy_foods]
   
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spicy_food_list = []
    for food in spicy_foods:
        if food["heat_level"] >= 5:
            spicy_food_list.append(food)
    return spicy_food_list
print(get_spiciest_foods(spicy_foods))        

def print_spicy_foods(spicy_foods):
        for food in spicy_foods:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')       
print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))        

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
#print(create_spicy_food(spicy_foods,{
    #     'name': 'Griot',
    #     'cuisine': 'Haitian',
    #     'heat_level': 10,
    # }))
    
