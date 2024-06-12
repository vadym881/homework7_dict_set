'hw_7.4'
def common_elements():
    multiple_by_3 = {num for num in range(100) if num % 3 == 0}
    multiple_by_5 = {num for num in range(100) if num % 5 == 0}
    common = multiple_by_3 & multiple_by_5
    return common

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print(common_elements())