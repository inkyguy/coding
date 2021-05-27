def lastRemaining(n, dp):
  # If dp[n] is already calculated
    if n in dp:
        return dp[n]
    # Base Case:
    if n == 1:
        return 1
    # Recursive Call
    else:
       
       # dp[n] = 2*(1+n//2- lastRemaining(n//2, dp)) for alternate even and odd condition
        dp[n] = 2*(lastRemaining(n//2, dp)) #repeated removal of odd positions (index starts from 1)
        
    # Return the value of dp[n]
    print (dp)
    return dp[n]
# Driver Code
N = 500000
dp = {}
print(lastRemaining(N, dp))
#1-1: 2-2: 3-2: 4-4 : 5-4: 6-4: 7-6: 8-8: 9-8: 