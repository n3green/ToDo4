candidatos = {'Nome: ', " ", 'Vaga: ', " " 'Resumo: ', " "}

def cadastro_candidatos():
        candidatos = {'Nome: ', " ", 'Vaga: ', " " 'Resumo: ', " "}
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
        candidatos['Nome: '] = nome.replace(" ")
        candidatos['Vaga: '] = vaga.replace(" ")
        candidatos['Resumo: '] = resumo.replace(" ")
        
