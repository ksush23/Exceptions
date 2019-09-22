n = input()
adj = dict()
level = dict()
list_of_exceptions = list()
printed_exceptions = list()


def bfs(s, par):
    level.update(dict([(s, 0)]))
    queue = [s]
    while queue:
        v = queue.pop(0)
        if v in adj:
            for w in adj.get(v):
                if w == par:
                    return True
                if level.get(w) is -1:
                    queue.append(w)
                    level.update(dict([(w, level.get(v) + 1)]))
    return False


for i in range(int(n)):
    line = input()
    if line.find(":") != -1:
        cur_class, parent = line.split(" : ")
        l = list(parent.split())

        newlist = []
        for i in range(len(l)):
            newlist.append(l[i])

        if cur_class in adj:
            previous = adj.get(cur_class)
            newlist.append(previous)

        new = dict([(cur_class, newlist)])
        adj.update(new)
        level.update(dict([(cur_class, -1)]))


for i in range(int(input())):
    cur_exception = input()
    if cur_exception in list_of_exceptions:
        if cur_exception not in printed_exceptions:
            print(cur_exception)
            printed_exceptions.append(cur_exception)
    if len(list_of_exceptions) == 0:
        list_of_exceptions.append(cur_exception)
    else:
        for exc in list_of_exceptions:
            for key in level:
                level.update(dict([(key, -1)]))
            if bfs(cur_exception, exc):
                if cur_exception not in printed_exceptions:
                    print (cur_exception)
                    printed_exceptions.append(cur_exception)
            else:
                if cur_exception not in list_of_exceptions:
                    list_of_exceptions.append(cur_exception)