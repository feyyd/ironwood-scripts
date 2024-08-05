def calculate_profit(base_rate, efficiency_speed_multiplier, profit_per_item):
    return base_rate * efficiency_speed_multiplier * profit_per_item

def calculate_percentage_difference(profit1, profit2):
    return (profit2 / profit1 - 1) * 100

def calculate_speed_multiplier(reference_item, target_item, ref_base_rate_multiplier, tar_base_rate_multiplier):
    # Unpack items
    _, ref_base_rate, ref_profit = reference_item
    _, tar_base_rate, tar_profit = target_item
    
    # Calculate profits with multiplier = 1, or pass adjusted rates (skill/efficiency diff %)
    ref_profit_value = calculate_profit(ref_base_rate, ref_base_rate_multiplier, ref_profit)
    tar_profit_value = calculate_profit(tar_base_rate, tar_base_rate_multiplier, tar_profit)
    
    return ref_profit_value / tar_profit_value

def create_comparison_table(skill_one_items, skill_two_items, skill_one_multiplier=1.0, skill_two_multiplier=1.0):
    # Create header
    header = ["Skill One / Skill Two"] + [item[0] for item in skill_two_items]
    
    # Calculate max width for each column
    col_widths = [max(len(str(row)) for row in col) for col in zip(*[header] + [
        [skill_one_item[0]] + [
            f"{(calculate_speed_multiplier(skill_one_item, skill_two_item, skill_one_multiplier, skill_two_multiplier) - 1) * 100:.1f}%"
            for skill_two_item in skill_two_items
        ]
        for skill_one_item in skill_one_items
    ])]
    
    # Create format string
    format_str = "  ".join(["{:<" + str(width) + "}" for width in col_widths])
    
    # Print table header
    print("\nComparison Table (values show required % increase in speed/efficiency for Skill Two):")
    print(format_str.format(*header))
    print("-" * (sum(col_widths) + 2 * (len(col_widths) - 1)))
    
    for skill_one_item in skill_one_items:
        row = [skill_one_item[0]] + [
            f"{(calculate_speed_multiplier(skill_one_item, skill_two_item, 1.0, skill_two_multiplier) - 1) * 100:.1f}%"
            for skill_two_item in skill_two_items
        ]
        print(format_str.format(*row))

# Functionally the same as above table version
def create_comparison_list(skill_one_items, skill_two_items, skill_one_multiplier = 1.0, skill_two_multiplier = 1.0):
    print("Required Total Speed/Efficiency Multipliers for Each Pair:\n")
    for skill_one_item in skill_one_items:
        for skill_two_item in skill_two_items:
            multiplier = calculate_speed_multiplier(skill_one_item, skill_two_item, skill_one_multiplier, skill_two_multiplier)
            print(f"{skill_one_item[0]:<{20}}: vs {skill_two_item[0]:<{20}} {(multiplier - 1) * 100:>{20}.1f}%")


skill_one = [
    ("Peony",      10 ),
    ("Tulip",      14 ),
    ("Rose",       20 ),
    ("Daisy",      26 ),
    ("Lilac",      32 ),
    ("Hyacinth",   38 ),
    ("Nemesia",    44 ),
    ("Snapdragon", 50 )
]

skill_two = [
    ("Copper",    4 ),
    ("Iron",      8 ),
    ("Silver",   12 ),
    ("Gold",     16 ),
    ("Cobalt",   20 ),
    ("Obsidian", 24 ),
    ("Astral",   28 ),
    ("Infernal", 32 )
]

skill_base_rate = [3600 / x for x in [4.1, 6.1, 8.1, 10.1, 12.1, 14.1, 16.1, 18.1]]
skill_one = [(*skill, rate) for skill, rate in zip(skill_one, skill_base_rate)]
skill_two = [(*skill, rate) for skill, rate in zip(skill_two, skill_base_rate)]


# List w/ same price/efficiency/speed
#create_comparison_list(skill_one, skill_one)

# List w/ different prices and same efficiency/speed
#create_comparison_list(skill_one, skill_two)

# List w/ different prices and different efficiency/speed
#create_comparison_list(skill_one, skill_two, 1, 2.5)

# Table format
# Table w/ same price/efficiency/speed
#create_comparison_table(skill_one, skill_one)

# Table w/ different prices and same efficiency/speed
#create_comparison_table(skill_one, skill_two)

# Intended use - Table w/ different prices and different efficiency/speed, ie: 25 skill levels (6.25%) and 2% from items
create_comparison_table(skill_one, skill_two, 1.0, 1.0825)
#create_comparison_table(skill_one, skill_two, 1.0, 2.5)
