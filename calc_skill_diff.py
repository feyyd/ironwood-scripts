def calculate_profit(base_rate, efficiency_speed_multiplier, profit_per_item):
    return base_rate * efficiency_speed_multiplier * profit_per_item

def calculate_percentage_difference(profit1, profit2):
    return (profit2 / profit1 - 1) * 100

def calculate_speed_multiplier_for_consistency(reference_item, target_item, ref_base_rate_multiplier = 1.0, tar_base_rate_multiplier = 1.0):
    # Unpack items
    _, ref_base_rate, ref_profit = reference_item
    _, tar_base_rate, tar_profit = target_item
    
    # Calculate profits with multiplier = 1, or pass adjusted rates (skill/efficiency diff %)
    ref_profit_value = calculate_profit(ref_base_rate, ref_base_rate_multiplier, ref_profit)
    tar_profit_value = calculate_profit(tar_base_rate, tar_base_rate_multiplier, tar_profit)
    
    # Calculate the required multiplier to match the percentage difference
    if tar_profit_value == ref_profit_value:
        return 1.0  # No adjustment needed
    else:
        return ref_profit_value / tar_profit_value

def print_speed_multipliers(skill_one_items, skill_two_items):
    print("Required Total Speed/Efficiency Multipliers for Each Pair:\n")
    for skill_one_item in skill_one_items:
        for skill_two_item in skill_two_items:
            multiplier = calculate_speed_multiplier_for_consistency(skill_one_item, skill_two_item)
            print(f"{skill_two_item[0]:<{20}}: vs {skill_one_item[0]:<{20}} {(multiplier - 1) * 100:>{20}.1f}%")

# Data for skill_two (name, base_rate, profit_per_item)
skill_one = [
    ("Peony",       3600 / 4.1,  10  ),
    ("Tulip",       3600 / 6.1,  14  ),
    ("Rose",        3600 / 8.1,  20 ),
    ("Daisy",       3600 / 10.1, 26 ),
    ("Lilac",       3600 / 12.1, 32 ),
    ("Hyacinth",    3600 / 14.1, 38 ),
    ("Nemesia",     3600 / 16.1, 44 ),
    ("Snapdragon",  3600 / 18.1, 50 )
]

# Data for skill_one (name, base_rate, profit_per_item)
skill_two = [
    ("Copper",   3600 / 4.1,  4  ),
    ("Iron",     3600 / 6.1,  8  ),
    ("Silver",   3600 / 8.1,  12 ),
    ("Gold",     3600 / 10.1, 16 ),
    ("Cobalt",   3600 / 12.1, 20 ),
    ("Obsidian", 3600 / 14.1, 24 ),
    ("Astral",   3600 / 16.1, 28 ),
    ("Infernal", 3600 / 18.1, 32 )
]

# same price and efficiency/speed
print_speed_multipliers(skill_one, skill_one)

# different prices same efficiency/speed
#print_speed_multipliers(skill_one, skill_two)

# different prices different efficiency/speed, ie: 25 skill levels (6.25%) and 2% from items
# print_speed_multipliers(skill_one, skill_two, 1.0, 1.0825)
