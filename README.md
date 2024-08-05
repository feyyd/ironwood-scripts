# README
```
skill_one = [
    ("Peony",        10  ),    ("Tulip",        14  ),
    ("Rose",         20  ),    ("Daisy",        26  ),
    ("Lilac",        32  ),    ("Hyacinth",     38  ),
    ("Nemesia",      44  ),    ("Snapdragon",   50  )
]

skill_two = [
    ("Copper",     4  ),    ("Iron",       8  ),    
    ("Silver",    12  ),    ("Gold",      16  ),
    ("Cobalt",    20  ),    ("Obsidian",  24  ),
    ("Astral",    28  ),    ("Infernal",  32  )
]
```
List view
```
def create_comparison_list(skill_one_items, skill_two_items, skill_one_multiplier = 1.0, skill_two_multiplier = 1.0):

create_comparison_list(skill_one, skill_one)

Peony               : vs Peony                                 0.0%
Peony               : vs Tulip                                 6.3%
Peony               : vs Rose                                 -1.2%
Peony               : vs Daisy                                -5.3%
Peony               : vs Lilac                                -7.8%
Peony               : vs Hyacinth                             -9.5%
Peony               : vs Nemesia                             -10.8%
Peony               : vs Snapdragon                          -11.7%
Tulip               : vs Peony                                -5.9%
Tulip               : vs Tulip                                 0.0%
Tulip               : vs Rose                                 -7.0%
Tulip               : vs Daisy                               -10.8%
Tulip               : vs Lilac                               -13.2%
Tulip               : vs Hyacinth                            -14.8%
Tulip               : vs Nemesia                             -16.0%
Tulip               : vs Snapdragon                          -16.9%
Rose                : vs Peony                                 1.2%
Rose                : vs Tulip                                 7.6%
Rose                : vs Rose                                  0.0%

create_comparison_list(skill_one, skill_two) # Different priced items comparison 

Peony               : vs Copper                              150.0%
Peony               : vs Iron                                 86.0%
Peony               : vs Silver                               64.6%

We would need 150% in efficiency and skill to make as much Peony with same skills.  Items take same time to create, copper gives 4g, Peony 10g.

- Modify skill_two efficiency/speed by 150% (1+1.5) to confirm
- 
create_comparison_list(skill_one, skill_two, 1.0, 2.5)

Peony               : vs Copper                                0.0%
Peony               : vs Iron                                -25.6%
Peony               : vs Silver                              -34.1%

With an increase of 150% from skills/speed, we reach parity of Copper/Peony.

Iron becomes more profitable than Peony, so much that there is an excess 25% of efficiency/speed (25% is 100 levels or ~3 building upgrades)
```
Table view and intended use
```
Different prices with different (skills) efficiency/speed, ie: 25 skill levels (6.25%) and 2% from items, with reminder of the 2.5 example for clarity

create_comparison_table(skill_one, skill_two, 1.0, 1.0825)
create_comparison_table(skill_one, skill_two, 1.0, 2.5)

Comparison Table (values show required % increase in speed/efficiency for Skill Two):
Skill One / Skill Two  Copper  Iron   Silver  Gold   Cobalt  Obsidian  Astral  Infernal
---------------------------------------------------------------------------------------
Peony                  130.9%  71.8%  52.1%   42.2%  36.3%   32.4%     29.6%   27.4%
Tulip                  117.3%  61.7%  43.1%   33.8%  28.3%   24.6%     21.9%   19.9%
Rose                   133.8%  73.9%  54.0%   44.0%  38.0%   34.0%     31.2%   29.0%
Daisy                  143.8%  81.3%  60.5%   50.1%  43.9%   39.7%     36.7%   34.5%
Lilac                  150.4%  86.3%  64.9%   54.2%  47.8%   43.5%     40.5%   38.2%
Hyacinth               155.2%  89.8%  68.1%   57.2%  50.6%   46.3%     43.2%   40.8%
Nemesia                158.8%  92.5%  70.4%   59.4%  52.7%   48.3%     45.2%   42.8%
Snapdragon             161.6%  94.6%  72.3%   61.1%  54.4%   49.9%     46.7%   44.3%

Comparison Table (values show required % increase in speed/efficiency for Skill Two):
Skill One / Skill Two  Copper  Iron    Silver  Gold    Cobalt  Obsidian  Astral  Infernal
-----------------------------------------------------------------------------------------
Peony                  0.0%    -25.6%  -34.1%  -38.4%  -41.0%  -42.7%    -43.9%  -44.8%
Tulip                  -5.9%   -30.0%  -38.0%  -42.0%  -44.5%  -46.1%    -47.2%  -48.1%
Rose                   1.2%    -24.7%  -33.3%  -37.7%  -40.2%  -42.0%    -43.2%  -44.1%
Daisy                  5.5%    -21.5%  -30.5%  -35.0%  -37.7%  -39.5%    -40.8%  -41.8%
Lilac                  8.4%    -19.3%  -28.6%  -33.2%  -36.0%  -37.9%    -39.2%  -40.2%
Hyacinth               10.5%   -17.8%  -27.2%  -32.0%  -34.8%  -36.7%    -38.0%  -39.0%
Nemesia                12.0%   -16.6%  -26.2%  -31.0%  -33.9%  -35.8%    -37.1%  -38.2%
Snapdragon             13.3%   -15.7%  -25.4%  -30.2%  -33.1%  -35.1%    -36.5%  -37.5%
```
