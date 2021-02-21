
# AppNewCredits
####################################

# Start server

# Abra o terminal e digite o seguinte comando:
# python manage.py runserver

# depois acesse:

# http://127.0.0.1:8000/admin
# User : Geek
# password : 18100707
# Ali você pode cadastrar usuários, e depois de
# cadastrar o usuário poderá cadastrar alguma dívida
# que o mesmo possa ter contraído, lembrando que o 
# compo 'Usuario' da tabela "Divida" é um ForeignKey
# da tabela 'Usuario'

# Acessando pela API
# Todos os métodos em uma view, 

# Para listar todos os usuarios e inserir
# novo usuario:

# http://127.0.0.1:8000/api/usuarios

# Para Deletar ou atualizar, onde '?' é o id 
# do usuario desejado:

# http://127.0.0.1:8000/api/usuarios/?

# Para listar todos as dividas e inserir
# nova divida:

# http://127.0.0.1:8000/api/dividas

# Para Deletar ou atualizar, onde '?' é o id 
# da divida desejada:

# http://127.0.0.1:8000/api/dividas/?
