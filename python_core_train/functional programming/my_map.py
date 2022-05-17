def mymap(func, *args):
    all_arg = list(args)
    min_len = len(all_arg[0])
    for arg in all_arg:
        if len(arg) < min_len:
            min_len = len(arg)
    print(all_arg)
    new_args = []
    i = 0
    while i < min_len:
        new_arg = []
        for arg in all_arg:
            new_arg.append(arg[i])
        i += 1
        new_args.append(new_arg)
    result = []
    print(new_args)
    for arg in new_args:
        result.append(func(*arg))
    return result
