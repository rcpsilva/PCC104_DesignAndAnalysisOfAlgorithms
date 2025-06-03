'''procedure BACKTRACK(solucao_parcial):
    se solucao_parcial é uma solução completa então
        processa(solucao_parcial)  # exibe, armazena ou conta a solução
        retorne
    fim-se

    para cada escolha possível e válida a partir de solucao_parcial faça:
        faça a escolha (adicione ao estado atual)
        BACKTRACK(nova solucao_parcial)
        desfaça a escolha (retorne ao estado anterior)
    fim-para
end procedure '''


def is_valid_choice(sol,v):

    if v in sol:
        return False

    linha = len(sol)

    for i in range(len(sol)):
        if abs(i-linha) == abs(sol[i]-v):
            return False
        
    return True

def backtracking(sol=[],n=8):

    print(sol)
    if len(sol)==n:
        print(sol)
    else:
        for choice in range(n):
            if is_valid_choice(sol,choice):
                sol.append(choice)
                backtracking(sol,n)
                sol.pop(-1)

if __name__ == '__main__':

    backtracking([],4)