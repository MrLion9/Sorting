import math

def bubbleSort(list):
    j=0
    while j<=(len(list)-1):
        k=0
        while k<=(len(list)-2):
            if list[k]>=list[k+1]:
                b=list[k]
                list[k]=list[k+1]
                list[k+1]=b
            k+=1
        j+=1
    print(list)
    return list

def combSort(list):
    reduct=math.floor(len(list)/1.247)
    while reduct>=1:
        k=0
        while (k+reduct)<=(len(list)-1):
            if list[k]>=list[k+reduct]:
                b=list[k]
                list[k]=list[k+reduct]
                list[k+reduct]=b
            k+=reduct
        reduct=math.floor(reduct/1.247)
    print(list)
    return list

def Merge(m, left, middle, right):
    low=left
    high=middle+1
    i=0
    b=[None]*(right-left+1)
    #print(b)
    #print(left,middle,right)
    while low<=middle and high<=right:
        if m[low]<=m[high]:
            b[i]=m[low]
            low+=1
        else:
            b[i]=m[high]
            high+=1
        i+=1
    #print(b)
    if low>middle:
        k=high
        while k<=right:
            b[i]=m[k]
            i+=1
            k+=1
    if low<=middle:
        k=low
        while k<=middle:
            b[i]=m[k]
            k+=1
            i+=1
    j=0
    while j<len(b):
        m[j+left]=b[j]
        j+=1
    #print (m)
    print(b)
    print(m)
    return m


def mergeSort(M):
    def merge_sort(m, left, right):
        if left==right:
            return m
        else:
            middle=math.floor((left+right)/2)
            merge_sort(m, left, middle)
            merge_sort(m, middle+1, right)
            Merge(m, left, middle, right)
    merge_sort(M, 0, len(M)-1)

def cocktail(list):
    left=0
    right=len(list)-1
    t=True
    while left<right and t:
        t=False
        l=left
        while l<right:
            if list[l]>list[l+1]:
                b=list[l]
                list[l]=list[l+1]
                list[l+1]=b
            l+=1
            t=True
        right-=1
        if t:
            r=right
            t=False
            while r>left:
                if list[r]<list[r-1]:
                    b=list[r]
                    list[r]=list[r-1]
                    list[r-1]=b
                r-=1
                t=True
        left+=1
    print(list)
    return list


array3=[5,3,2,6,23,5,132]

#bubbleSort(array3)
#combSort(array3)
#mergeSort(array3)
#cocktail(array3)


def countingSort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    pos = 0
    identity=0
    A[:] = []
    for number in range(scope):
        if C[pos]>1:
            identity+=(C[pos]-1)
        A += [number] * C[pos]
        pos += 1
    print(len(A)-identity)

#countingSort(array3)
cocktail(array3)