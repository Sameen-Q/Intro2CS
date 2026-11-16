# SavePoint 1: 变量与数据类型
name = "Sameen"
age = 18
height = 1.62
student_now = True

print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))

# SavePoint 2: 添加算术运算符 (Pizza 派对案例)
slices_per_student = 3
students = 20
enrolled_students = students + 2          # 加法 (+)
present_students = enrolled_students - 1  # 减法 (-)

total_slices_needed = present_students * slices_per_student # 乘法 (*)
cost_per_student = 500 / present_students                   # 除法 (/)

boxes_to_order = total_slices_needed // 8                   # 整除 (//)
leftover_slices = (boxes_to_order * 8) % present_students   # 取余 (%)

print("Total slices needed:", total_slices_needed)
print("Boxes to order:", boxes_to_order)
print("Leftover slices:", leftover_slices)
