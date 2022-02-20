list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
dict1 = list1[0]
values1 = set(dict1.values())
dict2 = list1[1]
values2 = set(dict2.values())
dict3 = list1[3]
values3 = set(dict3.values())
dict4 = list1[5]
values4 = set(dict4.values())
dict5 = list1[6]
values5 = set(dict5.values())
print(values1 | values2 | values3 | values4 | values5)
L = [{'V': values1}, {'V': values2}, {'VI': values3}, {'V': values4}, {'VIII': values5}]
print(L)