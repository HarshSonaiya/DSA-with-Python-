<a href="https://raw.githubusercontent.com/HarshSonaiya/DSA-with-Python-/Hashing/main/Separate chaining in Hashing _ Practice _ GeeksforGeeks.pdf">View PDF</a>

code :

#User function Template for python3

class Solution:
    
    #Function to insert elements of array in the hashTable avoiding collisions.
    def separateChaining(self, hashSize, arr, sizeOfArray):
        #Your code here
        hashTable = [[] for _ in range(hashSize)]
        
        # Iterate over each element in the input array
        for num in arr:
            # Compute the hash index
            index = num % hashSize
            # Insert the element in the appropriate list
            hashTable[index].append(num)
        
        return hashTable


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
#Back-end complete function Template for Python 3

def main():
        T=int(input())
        while(T>0):
            
            hashSize=int(input())
            sizeOfArray=int(input())
            arr=input().strip()
            arr=arr.split()
            arr=list(map(int,arr))
            
            obj = Solution()
            hashTable = obj.separateChaining( hashSize, arr, sizeOfArray)
            
            
            for i in range(len(hashTable)):
                if len(hashTable[i])>0:
                    print(str(i)+"->",end="")
                    for j in range(len(hashTable[i])-1):
                        print(str(hashTable[i][j])+"->",end="")
                    print(hashTable[i][len(hashTable[i])-1],end="")
                    print()
            T-=1

if __name__ == "__main__":
    main()

# } Driver Code Ends
