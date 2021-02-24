
def prob1():
    values = [[x,(x % 10)] for x in range(1,76)]
    for v in values:
        if(v[1] == 0):
            v[1] = 10

    for v in values:
        print(v)


