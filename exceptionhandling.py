# # x=int(input("eneter a number:"))
# # y=int(input("eneter a number:"))
# # try:
# #     print(x/y)
# # except ZeroDivisionError as e:
# #     print(e)
# # finally:
#     print("done")
# for i in range(5):
#     if i==3:
#         break
#     print(i)
# else:
#     print("done")

# try:
#     a=input("eneter a name:")
#     print(a)
# except valueError as e:
#     print(e)
# else:
#     print("done")

# a=int(input("eneter a number"))
# if a<0:
#     raise valueError("number is negative")
# else:
#     print(a)


# try:
#     l=[1,2,3,4,5,6,7,8,9,10]
#     print(l[11])
# except IndexError as i:
#     print(i)
# finally:
#     print("done")
while True:
    try:
        a=int(input("Enter a number"))
        print(a)
        break
    except ValueError as e:
        print(e)
    finally:
        print("Done")






