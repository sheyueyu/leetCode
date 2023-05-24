
def isPalindrome( x: int) -> bool:
    # 定义反转后的数字
    revesed_num = 0
    if x==0:
        return True
    if x <0 or x % 10 ==0:
        return False
    # 
    tmp = x
    while(tmp>revesed_num):
        revesed_num = revesed_num*10+x%10
        x = x//10 
    
    print(tmp==revesed_num)
    output = (tmp==revesed_num)
    return output
x  = -121
isPalindrome(x)

