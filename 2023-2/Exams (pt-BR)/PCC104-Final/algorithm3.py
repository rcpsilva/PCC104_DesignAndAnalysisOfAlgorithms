def function(C, sol=[]):

    if len(sol) == len(C):
        print(sol)
    else:
        for v in range(len(C)):
            function(C, sol + [v])