# # for sqr in range(11):
# #     print(sqr ** 2)

# # number = 1

# # while number <= 20:
# #     if number % 2 == 0:
# #         print(number)
# #     number += 1


#     # number % 2 == 0 
#     # if number != False:
#     #     print(f'{number}')


# # for div in range(50, 101):
# #     if div % 7 == 0:
# #         print(div)
# #         continue

# # for div in range(50, 101):
# #     if div % 7 == 0:
# #         print(div)
# #         break

# row = 5

# # for i in range(row):
# #     for j in range(i + 1):
# #         print(1 + j, end=" ")
# #     print("")

# # for i in range(row):
# #     for j in range(row - i - 1):
# #         print(" ", end=" ")
# #     for k in range(i + 1):
# #         print(1 + k, end=" ")
# #     print("")

# n = 5  # maximum number

# # Upper half of diamond
# for i in range(1, n + 1):
#     print("\t" * (n - i), end= "\t")
#     for j in range(1, i + 1):
#         print(j, end= "\t")
#     for j in range(i - 1, 0, -1):
#         print(j, end= "\t")
#     print("\t")

# # Lower half of diamond
# for i in range(n - 1, 0, -1):
#     print("\t" * (n - i), end="\t")
#     for j in range(1, i + 1):
#         print(j, end="\t")
#     for j in range(i - 1, 0, -1):
#         print(j, end="\t")
#     print("\t")

# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     print(f"Multiplication Table of {i} : \n")
#     for j in range(1, 11):
#         print( f"{i} * {j} = ", i * j  )

# num = 1

# while num <= 20:
#     if num % 2 == 0:
#         print(f" {num} is even number"  )
#     num += 1

# for i in range(1, 20):
#     if i == 5:
#         continue
#     print(i)    

# num = 1

# while num <= 10:
#     if num == 5:
#         num += 1
#         continue
#     print(num)
#     num += 1

# for i in range(50, 101):
#     if i % 7 == 0:
#         print(i)
#         break

# i = 50

# while i <= 100:
#     if i % 7 == 0:
#         i += 1
#         print(i)        
#         continue
# print(i)
# i += 1

i = int(input("Enter a number: "))

for i in range(1, i + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")