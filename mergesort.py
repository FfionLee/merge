list=["a","ga","b","t","l","k","c","ge","e"]

def merge(list):
    if len(list)>1:
        midpoint=len(list)//2
        left=list[:midpoint]
        right=list[midpoint:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
            print(list)
        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1
            print(list)
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
            print(list)

merge(list)
print(list)