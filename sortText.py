import math
# coding: utf8
text = open('text.txt', 'r').read()

trashlist = [',','.','(',')']
for i in trashlist:
    text=text.replace(i,"")

s=text.split()
identity=0

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

mergeSort(s)
#print(s)

def defineIdentities(sortList):
    pos=0
    while pos<(len(sortList)-1):
        if sortList[pos]==sortList[pos+1]:
            global identity
            identity+=1
        pos+=1

defineIdentities(s)
print("unique words:",len(s)-identity)
print("all:",len(s))