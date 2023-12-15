def function(C, sol=[]):

    if len(sol) == len(C):
        res = []
        for i in range(len(sol)):
            res = res + [sol[i]]
    else:
        for v in range(len(C)):
            function(C, sol + [v])