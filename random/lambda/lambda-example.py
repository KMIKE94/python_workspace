import pprint

country_weathers = (('Dublin', 15), ('Toronto', -2), ('Las Vegas', 31))

c_to_f = lambda data: (data[0], data[1]*(9/5)+ 32)

feh_wather=list(map(c_to_f, country_weathers))
print(feh_wather)