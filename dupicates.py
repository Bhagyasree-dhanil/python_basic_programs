"""
find duplicates names in the array
"""
name_array = ["bhagya", "sree", "dhanil", "sree", "dhath", "dhath", "padma"]

set_array=[]
dup_array=[]

for i, val in enumerate(name_array):
    if i == 0:
        set_array.append(val)
    elif val not in set_array:
        set_array.append(val)
    else:
        dup_array.append(val)

print("dup", dup_array,"set", set_array)
