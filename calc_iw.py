def calculate_profit(base_rate, efficiency_speed_multiplier, profit_per_item):
    return base_rate * efficiency_speed_multiplier * profit_per_item

def calculate_percentage_difference(profit1, profit2):
    return (profit2 / profit1 - 1) * 100

def create_comparison_table(items, speed_multiplier=1.0):
    profits = {name: calculate_profit(base_rate, speed_multiplier, profit) for name, base_rate, profit in items}
    
    # Sort items by profit
    sorted_items = sorted(profits.items(), key=lambda x: x[1])
    
    # Create and print the table
    print(f"{'Item':<10}", end="")
    for name, _ in sorted_items:
        print(f"{name:<10}", end="")
    print()
    
    for row_name, row_profit in sorted_items:
        print(f"{row_name:<10}", end="")
        for col_name, col_profit in sorted_items:
            if col_profit <= row_profit:
                print(f"{'-':^10}", end="")
            else:
                percentage = calculate_percentage_difference(row_profit, col_profit)
                print(f"{percentage:.2f}%".center(10), end="")
        print()

# Data for metal bars (name, base_rate, profit_per_item)
# 0 efficiency bars/hr
metal_bars = [
    ("Copper",   3600 / 4.1, 16),
    ("Iron",     3600 / 6.1, 32),
    ("Silver",   3600 / 8.1, 48),
    ("Gold",     3600 / 10.1, 64),
    ("Cobalt",   3600 / 12.1, 80),
    ("Obsidian", 3600 / 14.1, 96),
    ("Astral",   3600 / 16.1, 112),
    ("Infernal", 3600 / 18.1, 128)
]

# Data for wood types (name, base_rate, profit_per_item)
wood_types = [
    ("Pine",     3600 / 4.1, 4),
    ("Spruce",   3600 / 6.1, 8),
    ("Birch",    3600 / 8.1, 12),
    ("Teak",     3600 / 10.1, 16),
    ("Mahogany", 3600 / 12.1, 20),
    ("Ironbark", 3600 / 14.1, 24),
    ("Redwood",  3600 / 16.1, 28),
    ("Ancient",  3600 / 18.1, 32)
]

metal_speed_and_efficiency = 1.0525
print(f"Metal Bars Comparison (Speed {metal_speed_and_efficiency}):")
create_comparison_table(metal_bars, metal_speed_and_efficiency)

wood_speed_and_efficiency = 1.5525
print(f"\nWood Types Comparison (Speed {wood_speed_and_efficiency}):")
create_comparison_table(wood_types, wood_speed_and_efficiency)