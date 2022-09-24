# 1)................................................
# n=int(input("Enter number : "))
# r=0
# while n>0:
#     r=n%10
#     print(r,end="")
#     n//=10

# 2)...............................................
# n=int(input("Enter number : "))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
# if c==2:
#     print(n,"is a prime number")
# else:
#     print("not a prime number")


# 3) ................................................
# n=int(input("Enter number : "))
# for i in range (2,n+1):
#     if n>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#             else:
#                 print(i,end=" ")
#                 break  