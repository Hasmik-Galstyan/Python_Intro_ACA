# # # Տնային աշխատանք 2
#
# # 1. Ստեղծեք լիստ, օգտագործելով loop կամ list comprehension, որը կպարունակի մինչև 100 բոլոր թվերը։
# Ապա լուփի միջոցով print արեք միայն այն թվերը, որոնք բաժանվում են 7-ի:

my_list = []

# Create a list with 0 to 100 all numbers
for i in range(100):
    my_list.append(i)
print(my_list)

# Print number from the list devided by 7
for i in my_list:
    if i != 0 and i % 7 == 0:
        print(i)

# # 2. Գրեք նախորդ տնային աշխատանքի FizzBuzz-ը,
# սակայն լուփի միջոցով տպեք առաջին հարյուր թվերը կամ դրանց համապատասխանող բառը։
# Output-ը պիտի լինի այսպիսին՝

for num in range (0,100):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Buzz")
    elif num % 5 ==0:
        print("Fizz")
    else:
        print(num)

# # 3. Փոփոխեք նախորդ տնայինի առաջին առաջադրանքն այնպես, որ ջերմաստիճանը մուտքագրի user-ը։ Լուփի միջոցով այնպես արեք, որ ծրագիրը, որ ծրագիրը չավարտվի և անընդհատ հնարավոր լինի ջերմաստիճան մուտքագրել և կոնվերտացիան ստանալ։ Եթե user-ը ցանկանում է ծրագիրը դադարեցնել, կարող է հավաքել quit, և դուրս գալ (դրա մասին նույնպես զգուշացրեք նրան)։
# #
# # Հուշում․ օգտվեք ```input()``` ֆունկցիայից, որպեսզի հնարավոր լինի մուտքագրել ջերմաստիճանը։
# #
# # output-ը պետք է մոտավորապես այսպիսի բան լինի՝
# # ```
# # Enter a temperature in F or C units in this format, etc. 36C
# # Enter 'quit' to exit the program: 36C
# #
# # 36C  in Fahrenheit units is    96.80
# # ====================================================================================================
# # Enter a temperature in F or C units in this format, etc. 36C
# # Enter 'quit' to exit the program: 24F
# #
# # 24F  in Celsius units is      -4.44
# # ====================================================================================================
# # Enter a temperature in F or C units in this format, etc. 36C
# # Enter 'quit' to exit the program: 24F
# #
# # 24F  in Celsius units is      -4.44
# # ====================================================================================================
# # Enter a temperature in F or C units in this format, etc. 36C
# # Enter 'quit' to exit the program: 52F
# #
# # 52F  in Celsius units is      11.11
# # ====================================================================================================
# # Enter a temperature in F or C units in this format, etc. 36C
# # Enter 'quit' to exit the program: 245C
# #
# # 245C in Fahrenheit units is   473.00
# # ====================================================================================================
# # Enter a temperature in F or C units in this format, etc. 36C
# # Enter 'quit' to exit the program: quit
# #
# # Program is terminated. Bye!
# # ```
# #
# # Ուշադրություն դարձրեք ֆորմատավորմանը (օրինակ՝ ```'{:>4}'.format(some_var)```)։ Փորձեք այնպես գրել կոդը, որ output-ն ամբողջովին համապատասխանի օրինակին։
#
# # In[ ]:
#
#
# # 4. Առանց count() մեթոդի, Loop-ի օգնությամբ հաշվել, թե քանի 'a' կա բանաստեղծության տրված հատվածում

poem = """
O Captain! my Captain! our fearful trip is done,
The ship has weather’d every rack, the prize we sought is won,
The port is near, the bells I hear, the people all exulting,
While follow eyes the steady keel, the vessel grim and daring;
                         But O heart! heart! heart!
                            O the bleeding drops of red,
                               Where on the deck my Captain lies,
                                  Fallen cold and dead."""
#
# count = 0
# for i in poem:
#     if i == 'a':
#         count = count + 1
# print(f"The total number of 'a' character in given string is {count}")
#
#
# # # 5. Ստեղծել դատարկ լիստ, և այն լցնել մինչև 200-ը պարզ թվերով:
#
# lst = []
# for p_n in range (1,201):
#     for i in range (2,p_n+1):
#         if p_n % i == 0:
#             if p_n == i:
#                 lst.append(p_n)
#             else:
#                 break
# print(lst)
#
#
# # # 6. Ստեղծեք ձեր անձնական սորտավորող կոդը։ Տրված լիստը պետք է սորտավորեք նվազման կարգով առանց գործածելու sort() մեթոդը
# # #
# # # Output
# # # ```
# # # [9999, 9877, 242, 194, 98, 45, 8, 6]
# # # ```
# #
# # # In[44]:
# #
# #
#
# # lst = [194, 242, 9877, 98, 45, 6, 8, 9999]
# #
# # sorted_list = []
# # for i in lst:
# #     if
#
#
# # # 7. Ստեղծեք լիստ, որը կպարունակի առաջին 100 թվերը։ Այնուհետև ստեղծեք երկու նոր լիստ, որոնցից մեկը կպարունակի միայն առաջին լիստի զույգ թվերը, իսկ մյուսը՝ կենտ թվերը։
# #
# # # In[ ]:
# #
# #
# # # 8. Տրված է թիվ։ Այնպես արեք, որ ստանաք նոր թիվ, որը նախորդ թիվն է, թվանշանների տեղերը շրջած, օրինակ՝ 2451-ը պետք է դառնա 1542:
# #
# # # In[49]:
#
# # number = 7536
# # new_number = ''
# #
# # print("Given number", number)
# #
# while (number > 0):
#     digit = number % 10
#
#     number = number // 10
#     new_number += str(digit)
#
# print("Reversed number", int(new_number))
#
# # 9. Տպեք բազմապատկման աղյուսակը։ Կրկին ուշադրություն դարձրեք ֆորմատավորմանը։
# #
# # Output
# #
# # ```
# #   1   2   3   4   5   6   7   8   9  10
# #   2   4   6   8  10  12  14  16  18  20
# #   3   6   9  12  15  18  21  24  27  30
# #   4   8  12  16  20  24  28  32  36  40
# #   5  10  15  20  25  30  35  40  45  50
# #   6  12  18  24  30  36  42  48  54  60
# #   7  14  21  28  35  42  49  56  63  70
# #   8  16  24  32  40  48  56  64  72  80
# #   9  18  27  36  45  54  63  72  81  90
# #  10  20  30  40  50  60  70  80  90 100
# #  ```
#
# # In[ ]:
#
#
# # 10. Տպեք հետևյալ պատկերը․
# #
# # ```
# # * * * * * * * * * *
# # * * * * * * * * *
# # * * * * * * * *
# # * * * * * * *
# # * * * * * *
# # * * * * *
# # * * * *
# # * * *
# # * *
# # * ```
#
# # In[ ]:
#
#

# lst = [[], [], [], [], []]
# for i in range(5):
#
#   for j in range(5):
#     lst[i].append('*')
#
# print(lst)

