people_dict ={
    "小王":{
        "部门":"科技部",
        "工资":3000,
        "级别":1},
    "小周":{
        "部门":"市场部",
        "工资":5000,
        "级别":2},
    "小林":{
        "部门":"市场部",
        "工资":7000,
        "级别":3},
    "小张":{
        "部门":"科技部",
        "工资":4000,
        "级别":1},
    "小刘":{
        "部门":"市场部",
        "工资":6000,
        "级别":2},}
print(f"升职加薪前的部门工资是{people_dict}")
for key in people_dict:
    for key2 in people_dict[key]:
        if people_dict[key]["级别"] == 1:
            people_dict[key]["级别"] += 1
            people_dict[key]["工资"] += 1000

print(f"升职加薪后的部门工资是{people_dict}")

