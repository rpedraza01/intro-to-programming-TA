#unit_converter.py
to_meters_dict = {'ft': 3.28084, 'm': 1, 'km': .001, 'mm': 1000, 'cm': 100, 'in': 39.37, 'yd': 1.09, 'mi': .000621}
in_num = int(input("How many units of measurement do you have? > "))
in_unit = input("What unit of measurement do you have? > ")
out_unit = input("What type of unit do you want? > ")
meters = (in_num / to_meters_dict[in_unit])
out_num = (meters * to_meters_dict[out_unit])
print(f"{in_num} {in_unit} is equal to {out_num} {out_unit}, close enough")
