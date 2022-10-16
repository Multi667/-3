src = not False and True or False and not True
# result = not False and True or False and not True # избавляемся от отрицания
# result = True and True or False and False # избавляемся от логического "И"
# result = True or False # избавляемся от логического "ИЛИ"
result = True  # TODO подставить результат выражения

print(src == result)
