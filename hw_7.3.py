'hw_7.3'
def second_index(text: str, some_str):
    index_0 = text.find(some_str)
    if index_0 == -1:
        return None    
    index_1 = text.find(some_str, index_0 + len(some_str))
    if index_1 == -1:
        return None
    return index_1
assert second_index("sims", "s") == 3, 'Test1' 
assert second_index("find the river", "e") == 12, 'Test2' 
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4' 
print('ОК - Task3')
