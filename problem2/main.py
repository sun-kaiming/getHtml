long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# print(long_text)
dict = {}
list_text = long_text.split('\n')
dict['name'] = list_text[1]
dict['lei'] = list_text[2]

list2=[]
flag=0
list1=[]
temp={}
for index in range(3, len(list_text)-1):
    ch = list_text[index][0]
    if '1' <= ch <= '9':
        dict2 = {}
        if flag == 1:
            temp['isin'] = list2
            list2 = []
            dict2['title']=temp['title']
            dict2['isin'] = temp['isin']
            list1.append(dict2)
        temp['title'] = list_text[index][3:]
        flag = 1
    else:
        list2.append(list_text[index])
dict2={}
dict2['title']=temp['title']
dict2['isin'] = list2
list1.append(dict2)
dict['sub_fund']=list1
print(dict)