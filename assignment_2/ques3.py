# intput 2 list from user and merge then in one list and sort them

list1=list(map(int,input("enter your first list: ").split()))

list2=list(map(int,input("enter your second list: ").split()))

new_list=list1+list2
sorted=new_list.sort()
print(new_list)