# There is a small difference between lists and arrays in python
country_list = ["Ireland", "Colombia", "Nigeria", "Thailand", "Japan", "Denmark"]
print(country_list.index("Ireland"))

country_list.insert(3, "Russia")
print(country_list)

country_list.pop(2)
print(country_list)

country_list.remove("Thailand")
print(country_list)

country_list.reverse()
print(country_list)
print(type(country_list))

country_list.sort()
print(country_list)

country_list.reverse()
print(country_list)