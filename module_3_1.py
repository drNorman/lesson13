calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(st:str):
    count_calls()
    info = (len(st), st.upper(), st.lower())
    return info


def is_contains(st:str,lst:list[str]):
    count_calls()
    for i in lst:
        test_str = i
        if st.upper() == test_str.upper():
            return True
    return  False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
