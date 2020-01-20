#floor_wall_gen.py
import random
floor_wall_list = ['|', '_']
out_string = ''
for num in [0, 1, 2, 3]:
    out_string = out_string + random.choice(floor_wall_list)
    out_string = out_string + ' '
print(out_string)
