import DataBaser

def RegisterToDataBase(name, email, user, password):
    DataBaser.cursor.execute("""
    INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?) 
    """, (name, email, user, password))
    DataBaser.conn.commit()
    message = 'Cadastrado com Sucesso!'
    tam = len(message)
    print("""
    {} 
    {}
    {}
    """.format(tam*'=', message, tam*'='))


def Login(user, password):
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """, (user, password))
    Verify_Login = DataBaser.cursor.fetchone()
    try:
        if (user in Verify_Login and password in Verify_Login):
            print("Login realizado! Bem-vindo.")
            return True
    except:
        print("Usuário ou Senha não encontrados! ")
        return False


def verifica_escolha(escolha):
    if escolha != 1 or escolha != 2 or escolha != 3:
        print("Opção inexistente, escolha uma correta!")
        return True
    else:
        return False

def divisores_visual(mensagem):
    print("""
        {}
        {}
        {}
        """.format(len(mensagem)*'=', mensagem, len(mensagem)*'='))


#==============Programa Principal=========================
programa = False
while programa == False:
    print("""
    Seja bem-vindo ao Sistema de Login, escolha uma opção abaixo:
    1 - Login
    2 - Cadastro
    3 - Sair
    """)

    n=True
    while n == True:
        try:
            escolha = int(input("Digite a opção desejada: "))
            if escolha == 1 or escolha == 2 or escolha == 3:
                n=False
            else:
                mensagem = 'Opção inexistente, escolha uma correta!'
                divisores_visual(mensagem)
        except:
            mensagem = 'Opção inexistente, escolha uma correta!'
            divisores_visual(mensagem)






    if escolha == 1:
        username = input('Usuário: ')
        password = input('Senha: ')
        programa = Login(username, password)

    if escolha == 2:
        i=True
        while i == True:
            name = input('Digite o seu nome: ')
            if name == '':
                message = 'Insira um valor válido!'
                divisores_visual(message)
            else:
                i = False
        i = True
        while i == True:
            email = input('Digite o seu email: ')
            if email == '':
                message = 'Insira um valor válido!'
                divisores_visual(message)
            else:
                i = False
        i = True
        while i == True:
            user = input('Digite o seu usuário: ')
            if user == '':
                message = 'Insira um valor válido!'
                divisores_visual(message)
            else:
                i = False
        i = True
        while i == True:
            password = input('Digite a sua senha: ')
            if password == '':
                message = 'Insira um valor válido!'
                divisores_visual(message)
            else:
                i = False
        RegisterToDataBase(name, email, user, password)
    if escolha == 3:
        message="Obrigado por utilizar o Sistema de Login! See you soon!"
        divisores_visual(message)
        break

