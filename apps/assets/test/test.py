#
#
# #输入
# input_exam= "3520 4 3 89 56 88 3521 9 90 1 99 2 87"
#
# #输出格式有序列
# output_exam1="""
# 4
# 1 2 3 4
# 87 88 89 90
# """
# #输出格式无序列
# output_exam2="0"
#
#
# len_arr=0
#
#
# input_arr=input("请输入数组")
#
# input_list = input_arr.split(" ")
#
# input_list = list(map(int,input_list))
# inputlist_sort= sorted(input_list)
#
# inputlist_sort.append(0)
#
#
# ##进行排序查找
#
# len_lar=0
# res_list=[]
# pre_number =1
#
# fin_list=[]
# fin_len_arr=0
# for  i  in inputlist_sort:
#     if i-pre_number==1 :
#         if pre_number not in res_list and pre_number!=0:
#             res_list.append(pre_number)
#         pre_number=i
#         len_arr+=1
#         res_list.append(i)
#         # print(res_list)
#
#     else:
#         if len_arr>=1:
#             if len_arr>=fin_len_arr:
#                 fin_len_arr=len_arr
#             # len_lar=len_arr
#             # fin_len_arr=len_arr
#                 fin_list.append(res_list)
#             # print(fin_list)
#             # print("fin")
#             res_list=[]
#             len_arr=0
#             # pre_number=i
#         pre_number = i
#         # res_list.append(pre_number)
#         # print(pre_number)
#
#
# if fin_len_arr>1:
#
#     print(fin_len_arr+1)
#
#     for j in fin_list:
#         for v in j:
#             fin_v=str(v)+" "
#             print(str(v),end=" ")
#
#         print("")
# else:
#     print(0)

import os

print(os.getcwd())
os.chdir("E:\迅雷下载\.1a6d47fcfa4f4d84b84130a35135add7")

l = os.listdir()
# l.sort()
print(l)

num = len(os.listdir())//10

l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l2=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




for i in range(len(l)):
    for k in range(len(l)):
        i_num = int(l[i].split(".")[0])
        k_num = int(l[k].split(".")[0])
        print(i_num,k_num)

        if i_num<k_num:
            l[i],l[k] = l[k],l[i]


print(l)



# n = 0
# for i in range(num+1):
#
#
#     index = i//25
#
#     if index>25:
#         index = index%25
#
#     tmp=""
#     if n>25:
#         n=0
#         tmp+=l2[index]
#
#     sec_name = l2[n]
#
#
#
#     first_name = l1[index]+tmp
#     n+=1
#     os.rename(os.listdir()[i],(first_name+sec_name+".ts"))
#
#     # os.listdir()
#
#
# print(os.listdir())
#
# for i in os.listdir():
#     print(i )


#aaa


list

