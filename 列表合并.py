my_list=[
{1: [2,3,4], 2:3, 3:5, 4:[5,5, 6]},
{2: [1, ], 3:[1,2],4:[6,7], 5:5}
]

my_dict=my_list[0]


for var in my_list[1:]:
    # print(var)
    for key,value in var.items():


        if key in my_dict.keys():
            if isinstance(my_dict[key],int):

                my_dict[key]=[value]
            else:
                my_dict[key].extend(value)
        else:
            my_dict[key]=value


print(my_dict)




