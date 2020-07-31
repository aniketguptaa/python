# kwargs (keyword arguments)
# **kwargs (double star operator)

# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} : {v}")
# func(first_name = "Carry", second_name = "Niket")

#using kwargs in python

# def kwargss(**kwargs):
#     for keys, values in kwargs.items():
#         print(f"Name is {keys} and role is {values}")
# staff = {"Krishna":"Lord", "Ravan": "evil", "sita":"mata"}
# kwargss(**staff)

# A more realistic example (code readability index : 75%)
# def students_marks(**marks):
#     for keys , values in marks.items():
#         print(f"Name is {keys} and marks is {values}")
# students = {"Shubham": 86, "Manish":88, "Rajesh":90}
# students_marks(**students)

# a more and more realistic example (use to make code more readable cri = 90%)

# def masala(**brands):
#     for brand_names, turnover in brands.items():
#         print(f"Brand name is {brand_names} and annual turnover is {turnover}\n")
# # key = brand names
# # values = companie's turnover
# masala_brands = {"Everest":250000, "MDH":256984, "Rajesh Masales":256964,
# "cookme":259444, "Patanjali Masales":264965244}
# masala(**masala_brands)

