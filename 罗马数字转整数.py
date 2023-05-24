class Solution:
    def romanToInt(self, s: str) -> int:
        pass
        
    

roma = ["I","V","X","L","C","D","M"]
roma_values = [1,5,10,50,100,500,1000]
rama_value_map_dict = dict(zip(roma,roma_values))
s = "IVI"
s_list = list(s)
s_list

value_sum = 0
for i,item in enumerate(s_list):
    value_l = rama_value_map_dict[item]  # 左边的value
    if i < len(s_list)-1:
        value_r = rama_value_map_dict[s_list[i+1]] # 右边的value
        if value_l <value_r:
            # 左右合并起来能组成值
            value_sum = value_sum-value_l
        else:
            value_sum = value_sum+value_l
    else:
        value_sum= value_sum+value_l
value_sum

