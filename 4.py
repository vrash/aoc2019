ans = 0
for pwd in range(108457,562041+1):
    digits = [int(x) for x in str(pwd)]
    pair = any([(i==0 or digits[i]!=digits[i-1]) and digits[i]==digits[i+1] and (i==len(digits)-2 or digits[i]!=digits[i+2]) for i in range (len(digits)-1)])
    #largerpair = any([digits[i]==digits[i+1] and (digits[i]==digits[i+2] or digits[i+1]==digits[i+2]) for i in range (len(digits)-2)])
    dec = any([digits[i] > digits[i+1] for i in range (len(digits)-1)])
    if pair and not dec:
        ans += 1

print (ans)
