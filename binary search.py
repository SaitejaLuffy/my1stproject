def binsearch(lst,n):
    l= 0
    u= len(lst)-1

    while l<= n:
      mid=(l+u)//2
      if lst[mid]==n:
         return mid
      elif lst[mid]<n:
           l=mid+1
      else:
           u=mid-1        
    return -1 
lst=[4,7,8,12,45,67,68,66]
n = 45

pos =binsearch(lst,n)

if pos!=-1:
    print("found at ",pos+1)
else:
    print("not found") 