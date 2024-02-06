# Q1
# l=108
# h=33
# for c in range(h+1):
#     r=h-c
#     if 4 * r+2 * c == l and r>=0:
#         break
# print("Chickens are : ",c)
# print("Rabbits are : ",r)


# Q2

# t_mango=int(input())
# d1=t_mango//3
# extra=t_mango%3
#
# d2=d1+extra
# extra2=d2%3
# d3=d2//3
# extra3=d3
#
# final=d1+d2+d3
# rem=t_mango-final
# print(f"Daughter 1:  {d1}")
# print(f"Daughter 2:  {d2}")
# print(f"Daughter 3:  {d3}")
# print(f"final:  {final}")















# Q3
# r=int(input())
# c=int(input())
#
# mat=[[int(input("element")) for j in range(c)] for i in range(c)]
#
# trans=[[0 for i in range(r)] for j in range(c)]
# print()
# print("Matrix:")
# for i in mat:
#     print(i)
# for i in range(r):
#     for j in range(c):
#         trans[j][i]=mat[i][j]
#     print()
# print("Transpose Matrix:")
#
# for i in trans:
#     print(i)