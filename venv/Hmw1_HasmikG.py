# # Task 1. Տրված է ջերմաստիճան string-ով։
# # Ստուգել ֆարենհայթով (F) է ջերմաստիճանը, թե ցելսիուսով (C)
# # և փոխարինել համապատասխանաբար ցելսիուսով կամ ֆարենհայթով։
#
# t = '96.8F'
# n = float(t[0:t.find("F")])
# print (n)
#
# if 'F' in t:
#     C = (5/9) * (n - 32)
#     print(f"{t} is in Farenheit units, Celsius is {C}")
# elif 'C' in t:
#     F = 9/5 * n + 32
#     print(f"{t} is in Celsius units,Farenheit is {F}")
#
#
# # # Task 2. Տրված է լինելու int տիպի փոփոխական։ Ստուգել,
# # # եթե թիվը բաժանվում է 5-ի, տպել 'Fizz',
# # # եթե բաժանվում է 3-ի, տպել 'Buzz',
# # # իսկ եթե բաժանվում է և 5-ի, և 3-ի, տպել 'FizzBuzz'։
# # # Այլապես տպել հենց թիվը։
#
#
# # number = int(input ("Please input number:"))
# #
# # if number % 5 == 0 & number % 3 == 0:
# #     print("FizzBuzz")
# # elif number % 3 == 0:
# #     print("Buzz")
# # elif number % 5 ==0:
# #     print("Fizz")
# # else:
# #     print(number)
#
# # # Task 3․ Տրված է աշակերտի գնահատանները dictionary-ով։
# # # Հաշվել արդյունարար գնահատականը (գումարը) և ստուգել - եթե արդյունարար գնահատականը 40-ից ցածր է, տպում ենք Fail,
# # # եթե 41-60 է, տպել Satisfactory, եթե 61-80՝ Good,
# # # իսկ 81-100-ի դեպքում՝ Outstanding:
# # # Եթե գնահատականը 100-ից բարձր է, կամ բացասական է՝ տպել "Something's wrong with the input":
# # # Փորձեք տարբեր գնահատականներ, որ վստահ լինեք ամեն ինչ ճիշտ է։
#
# # grades = {'Math': 0,
# #           'Physics': 15,
# #           'Geography': 20,
# #           'History': 20,
# #           'Geometry': 0}
# #
# # grades_result = sum(grades.values())
# # print(grades_result)
# #
# # if grades_result <= 40:
# #     print("Fail")
# # elif grades_result in range (41,60):
# #     print("Satisfactory")
# # elif grades_result in range (61,80):
# #     print("Good")
# # elif grades_result in range (81,100):
# #     print("Outstanding")
# # elif grades_result > 100 or grades_result < 0:
# #     print('Something went wrong')
# # else:
# #     print(grades_result)
#
# poem = """
# O Captain! my Captain! our fearful trip is done,
# The ship has weather’d every rack, the prize we sought is won,
# The port is near, the bells I hear, the people all exulting,
# While follow eyes the steady keel, the vessel grim and daring;
#                          But O heart! heart! heart!
#                             O the bleeding drops of red,
#                                Where on the deck my Captain lies,
#                                   Fallen cold and dead."""

poem = """
O Captain! my Captain! our fearful trip is done,
The ship has weather’d every rack, the prize we sought is won,
The port is near, the bells I hear, the people all exulting,
While follow eyes the steady keel, the vessel grim and daring;
                         But O heart! heart! heart!
                            O the bleeding drops of red,
                               Where on the deck my Captain lies,
                                  Fallen cold and dead."""

count = 0
for char in poem:
    if char.lower() == 'a':
        count+=1
    print(count)