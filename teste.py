import cadastrocandidato as cad_cand

def menu_inicial ():
    i = True
    while i:
        print ()
        print ('-' * 20)
        print ('Bem vindo ao app de busca de curriculos!')
        print ('-' * 20)
        print ()
        print ('Menu de opcoes:')
        print ('[1] Cadastrar candidatos')
        print ('[2] Buscar Candidatos')
        print ('[3] Digite "3" para finalizar o atendimento')
        print ()
        opcoes = input('Escolha uma opcao acima: ')
        if opcoes == '1':
            cad_cand
        elif opcoes == '2':
            pass  
        elif opcoes == '3':
            i = False


menu_inicial()