candidatos = {'Nome' : '','Vaga': '','Resumo': ''}
lista_candidatos = [candidatos]
chave_analista = ['Python', 'PowerBL', 'SQL', 'Boa comunicacao']
chave_cientista = ['Python', 'Banco de dados', 'Machine Learning', 'Resolução De Problemas', 'Estatística']
resumo = []


def cadastro_candidatos():
        print () 
        print ('-' * 20)
        nome = input ('Qual o nome do candidato? ')
        print ('-' * 20)
        print ()
        print ('-' * 20)
        vaga = input ('Para qual vaga ele esta se inscrevendo? ')
        print ('-' * 20)
        print ()
        print ('-' * 20)
        resumo = input ('Escreva um pequeno resumo do candidato: ')
        print ('-' * 20)
        print ()
        
        for x in candidatos:
            if (x == 'Nome:'):
                candidatos['Nome:'] = nome
            elif (x == 'Vaga:'):
                candidatos['Vaga:'] = vaga
            elif (x == 'Resumo:'):
                candidatos['Resumo:'] = resumo
        return menu_inicial()
        
        

                
def buscar_candidato():
    print ()
    print ('-' * 20)
    if resumo == chave_analista or chave_cientista:
        print (lista_candidatos)
    
        
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
            cadastro_candidatos()
        elif opcoes == '2':
            buscar_candidato()
        elif opcoes == '3':
            i = False


menu_inicial()