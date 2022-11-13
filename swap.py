def swap_list(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
    
    
List = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    List.append(item)
#print("User list is ", list)    


pos1, pos2  = n//2 , n
 
#print(swap_list(List, pos1-1, pos2-1))