
# def isFourLetters(lst):
#     result = []
#     for x in lst:
#         if len(x) == 4:
#             result.append(x)
#     return result
# print(isFourLetters(["Tomato", "Potato", "Pair"]))
# print(isFourLetters(["Kangaroo", "Bear", "fox"]))
# print(isFourLetters(["Ryan", "Kieran", "Jason", "Matt"]))



# def firstclass(lst):
#     a = lst.pop(0)
#     b = lst.pop(-1)
#     return a, b
#
# print(firstclass([5,10,15,20,25]))
# print(firstclass(["edabit",13,'null',"false",'true']))
# print(firstclass(["undefined",4,6,"hello","null"]))



# def get_budgets(dict):
#     result = 0
#     for person in dict:
#         for key, value in person.items():
#             if key == 'budget':
#                 result += value
#     return result
#
# print(get_budgets([
#     {"name":"John", "age":21, "budget":23000},
#     {"name":"Steve", "age":32, "budget":40000},
#     {"name":"Martin", "age":16, "budget":2700}
#     ]))
