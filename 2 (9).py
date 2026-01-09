# 32. Rat in a House - PrepInsta
def count_paths(m, n):
    # Create DP table
    dp = [[0] * n for _ in range(m)]
    
    # Initialize first row and column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Fill DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

# Test
print(f"Paths in 3x3 grid: {count_paths(3, 3)}")
print(f"Paths in 4x4 grid: {count_paths(4, 4)}")