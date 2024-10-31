def getData(arg):
    user_input = input(f'enter {arg}')
    return user_input
def output(data):
    data = ['name','level']
    for i in range(len(data)):
        getData(data[i])
output(getData())