
user_input = input("Please Enter Roman Number: ").upper()
arabic_integer = []
result = 0

not_roman_list = [
    'LL', 'VV', 'DD', 'MMMM', 'IIII', 'CCCC', 'XXXX',
    'IIX', 'IXC', 'IVI', 'IL', 'IC', 'ID', 'IM', 'IXX', 'IXV', 'IXL', 'IIV', 'IXI', 'IVV',
    'VIX', 'VX', 'VL', 'VC', 'VD', 'VM', 'VIV',
    'XCM', 'XCD', 'XCX', 'XD', 'XM', 'XLX', 'XCC', 'XCL', 'XXL', 'XXC',
    'LXC', 'LC', 'LD', 'LM', 'LXL',
    'CMD', 'CCM', 'CMC', 'CDC', 'CMM', 'CCD',
    'DM', 'DCM', 'DCD',
]

roman_list = ["I", "V", "X", "L", "C", "D", "M"]

for c in range(len(not_roman_list)):
    while not_roman_list[c] in user_input:
        print("wrong")
        user_input = input("Please Enter Roman Number: ").upper()

for r in range(len(user_input)):
    while user_input[r] not in roman_list:
        print("wrong")
        user_input = input("Please Enter Roman Number: ").upper()

roman_dict ={
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

for el in user_input:
    arabic_integer.append(roman_dict[el])

i = 0

while i < len(arabic_integer) - 1:
    if arabic_integer[i] < arabic_integer[i + 1]:
        result += arabic_integer[i + 1] - arabic_integer[i]
        i += 2
    else:
        result += arabic_integer[i]
        i += 1

if i == len(arabic_integer) - 1:
    result += arabic_integer[i]
if result >= 4999:
 print('Over 4000, not correct !')
elif result < 4999:
    print(result)








