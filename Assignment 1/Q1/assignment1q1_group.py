# Ryan Lu, Anthony Thornton, Carla Madriz
# Group 9
# Dr. Sampson Akwafuo
# CPSC 335-04
# 02/25/2024

# Emails: rlu132@csu.fullerton.edu, anthonythornton140@csu.fullerton.edu, cmadriz@csu.fullerton.edu	

def swap(i,j,arr):
    # swap the elements at index i and j in vector arr
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

def min_swaps(arr):
    n = len(arr)
    total = 0
    # iterate through every other element in the list
    for i in range(0,n,2):
        # find value of the pair i is associated with
        value = [1,-1][arr[i]%2] + arr[i]
        # if the value of the next element is equal to the current element's pair, i.e. the 2 make a pair, then skip this iteration
        if (value == arr[i+1]):
            continue
        # find the index of the correct element to make a pair
        partnerindex = arr.index(value)
        # swap the elements so that a pair is made
        arr=swap(i+1,partnerindex,arr)
        total +=1
    return total

sample1 = [0,2,1,3]
print("Sample Array 1:",sample1)
print("Minimum number of swaps:",min_swaps(sample1))

sample2 = [3,2,0,1]
print("Sample Array 1:",sample2)
print("Minimum number of swaps:",min_swaps(sample2))

arr2 = [0,4,1,6,3,2,9,7,5,8] 
print("Example Array 3:",arr2)
print("Minimum number of swaps:",min_swaps(arr2))
#10 total nums w/ 8 wrong 2 correct 3 swaps
# 0,4,1,6,3,2,9,7,5,8
# 0,8,1,6,3,2,9,7,5,6
# 0,7,1,6,3,2,9,8,5,6
# 0,1,7,6,3,2,9,8,5,6

arr3 = [0,4,8,6,3,2,9,7,5,1]
print("Example Array 3:",arr3)
print("Minimum number of swaps:",min_swaps(arr3))
#10 total nums w/ 8 wrong 2 correct 2 swaps
# 0,4,8,6,3,2,9,7,5,1
# 0,1,8,6,3,2,9,7,5,4
# 0,1,7,6,3,2,9,8,5,4


