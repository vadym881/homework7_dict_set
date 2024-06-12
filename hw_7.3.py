'hw_7.3'
def second_index(text: str, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return -1
    
    second_index = text.find(some_str, first_index + len(some_str))
    return second_index
assert second_index("sims", "s") == 3, 'Test1' 
assert second_index("find the river", "e") == 12, 'Test2' 
# assert second_index("hi", "h") is None, 'Test3' #AssertionError
assert second_index("Hello, hello", "lo") == 10, 'Test4' 
print('ОК')

sentence = input('Enter sentence: ')
print(second_index(sentence, 's'))