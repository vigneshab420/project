# 25. Difference Between Sums - PrepInsta
def difference_sum(limit, n):
    sd = 0  # sum divisible
    snd = 0  # sum non-divisible
    
    for i in range(1, limit + 1):
        if i % n == 0:
            sd += i
        else:
            snd += i
    
    return abs(sd - snd)

# Test
print(f"Difference for limit=20, n=4: {difference_sum(20, 4)}")