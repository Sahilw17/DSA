# You are given two arrays A and B of length N 
# . You can select any subarray and then sort the elements in ascending order of that subarray for arrays A and B .
# Find the minimum length of the subarray you can choose to make   A and B  same after performing the operation.
# A  and B  are permutations of each other.

# A2 = [1, 3, 2, 4]
# B2 = [1, 2, 3, 4]
#output=2 as first and last index are same

t=int(input())

for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))

    left=0

    while left<n and a[left]==b[left]:
        left+=1

    right=n-1

    while right>=0 and a[right]==b[right]:
        right-=1

    if left>right:
        print(0)
    else:
        sub_A=a[left:right+1]
        sub_B=b[left:right+1]
        if sorted(sub_A)==sorted(sub_B):
            print(right-left+1)
        else:
            print(-1)
