convidados_da_festa= ['Maria', 'João', 'Ana', 'Carlos', 'Mariana']

status_presenca= {}

print('---Verificação da Lista de Convidados')

lista_de_chegadas= ['João', 'Ana', 'Pedro', 'Maria']

for pessoa in lista_de_chegadas:
    if pessoa in convidados_da_festa:
        print(f'Olá, {pessoa}! Bem-vindo(a) á festa.')
        status_presenca[pessoa]= 'Confirmado'
    
    else:
        print(f'Desculpa, {pessoa}. Seu nome não está na lista')
        status_presenca[pessoa]= 'Não convidado'

    
