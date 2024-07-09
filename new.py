

# def test(data):
    # print(**data)

def test(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

numbers = [1, 2, 3]
unpacked_numbers = [*numbers]
# print(unpacked_numbers)

# def test1(name, rollno):
    # print(name, rollno)
def test1(**kwargs):
    print(kwargs)
# test(1,11,12,helo="1")
test1(**{'name':'Angshu', 'rollno':2})
