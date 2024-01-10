import pickle
utilizadores = []

#Funçao que carrega uns dados de um ficheiro para a lista utilizadores usando o pickle.
def carregar_dados():
    ficheiro = open("dados.pkl", "rb")
    for cliente in pickle.load(ficheiro):
        utilizadores.append(cliente)
    ficheiro.close()

def guardar_dados():
    ficheiro = open("dados.pkl", "wb")
    pickle.dump(utilizadores, ficheiro)
    ficheiro.close()

def apagar_dados():
    ficheiro = open("dados.pkl", "wb")
    pickle.dump([], ficheiro)
    ficheiro.close()

#Funçao que verifica se o elementos na string sao numeros e se nao forem o utilizador tem de escrever outra vez até serem.
def verifica_numeros(string):
    while True:
        if string.isdigit():
            return string
        else:
            string = input("Caracteres inválidos. Tente outra vez: ")

#Funçao que verifica se o elementos na string sao letras e se nao forem o utilizador tem de escrever outra vez até serem.
def verifica_letras(string):
    while True:
        if string.isalpha():
            return string
        else:
            string = input("Caracteres inválidos. Tente outra vez: ")


def inserir_cliente():
    cliente = {}
    n_instalacao_k = "Nº de instalação"
    nome_cliente_k = "Nome do cliente"
    morada_k = "Morada"
    contato_k = "Contato"
    nif_k = "NIF"
    calibre_k = "Calibre"
    tarifa_social_k = "Existe tarifa social"

    if len(utilizadores) == 0:

        n_instalacao_v = input("Insira o nº de instalação: ")
        verifica_numeros(n_instalacao_v)
        nome_cliente_v = input("Insira o nome do cliente: ")
        verifica_letras(nome_cliente_v)
        morada_v = input("Insira a morada: ")
        contato_v = input("Insira o contato: ")
        verifica_numeros(contato_v)
        nif_v = input("Insira o NIF: ")
        verifica_numeros(nif_v)
        cliente[n_instalacao_k] = n_instalacao_v
        cliente[nome_cliente_k] = nome_cliente_v
        cliente[morada_k] = morada_v
        cliente[contato_k] = contato_v
        cliente[nif_k] = nif_v
        while True:
            calibre_v = int(input("Insira o Calibre: "))
            cliente[calibre_k] = calibre_v
            if calibre_v > 100:
                print("Calibre impossível. Tente outro")
            else:
                break

        print("1) Sem tarifa social")
        print("2) Com tarifa social")
        tarifa_social_v = input("Insira se o cliente tem tarifa social: ")
        verifica_numeros(tarifa_social_v)
        tarifa_social_v = tarifa_social_v.strip()
        if tarifa_social_v == "1":
            cliente[tarifa_social_k] = "Sem"
        elif tarifa_social_v == "2":
            cliente[tarifa_social_k] = "Com"

        utilizadores.append(cliente)

    elif len(utilizadores)>0:

        lista_instalacao = []
        lista_nome = []
        lista_morada = []
        lista_contato = []
        lista_nif = []

        for i in range(len(utilizadores)):
            lista_instalacao.append(utilizadores[i]["Nº de instalação"])
            lista_nome.append(utilizadores[i]["Nome do cliente"])
            lista_morada.append(utilizadores[i]["Morada"])
            lista_contato.append(utilizadores[i]["Contato"])
            lista_nif.append(utilizadores[i]["NIF"])

        while True:
            n_instalacao_v = input("Insira o nº de instalação: ")
            verifica_numeros(n_instalacao_v)
            cliente[n_instalacao_k] = n_instalacao_v
            if n_instalacao_v in lista_instalacao:
                print("Já existe esse Nº de instalação. Tente outro.")
            else:
                break

        while True:
            nome_cliente_v = input("Insira o nome do cliente: ")
            verifica_letras(nome_cliente_v)
            cliente[nome_cliente_k] = nome_cliente_v
            if nome_cliente_v in lista_nome:
                print("Já existe esse Nome. Tente outro.")
            else:
                break

        while True:
            morada_v = input("Insira a morada: ")
            cliente[morada_k] = morada_v
            if morada_v in lista_morada:
                print("Já existe essa Morada. Tente outra.")
            else:
                break

        while True:
            contato_v = input("Insira o contato: ")
            verifica_numeros(contato_v)
            cliente[contato_k] = contato_v
            if contato_v in lista_contato:
                print("Já existe esse Contato. Tente outro.")
            else:
                break

        while True:
            nif_v = input("Insira o NIF: ")
            verifica_numeros(nif_v)
            cliente[nif_k] = nif_v
            if nif_v in lista_nif:
                print("Já existe esse Nif. Tente outro.")
            else:
                break

        while True:
            calibre_v = int(input("Insira o Calibre: "))
            cliente[calibre_k] = calibre_v
            if calibre_v > 100 :
                print("Calibre impossível. Tente outro.")
            else:
                break

        print("1) Sem tarifa social")
        print("2) Com tarifa social")
        tarifa_social_v = input("Insira se o cliente tem tarifa social: ")
        verifica_numeros(tarifa_social_v)
        tarifa_social_v = tarifa_social_v.strip()
        if tarifa_social_v == "1":
            cliente[tarifa_social_k] = "Sem"
        elif tarifa_social_v == "2":
            cliente[tarifa_social_k] = "Com"

        utilizadores.append(cliente)

    return "Cliente inserido"


def chave_nome(d):
    return d["Nome do cliente"]

def consultar_cliente():
    while True:
        print("1) Consultar todos os clientes")
        print("2) Consultar só um cliente")
        print("3) Voltar atrás")

        funcionalidades = input("Escolha a funcionalidade: ")
        funcionalidades = funcionalidades.strip()
        if funcionalidades == "1":
            return sorted(utilizadores,key=chave_nome)
        elif funcionalidades == "2":
            for cliente in utilizadores:
                nome = input("Insira o nome do cliente: ")
                valores = cliente.values()
                if (nome in valores):
                    
                    return cliente
        elif funcionalidades == "3":
            break
        else:
            print("Opção invalida. Tente outra funcionalidade")

def eliminar_cliente():
    nome = input("Insira o nome do cliente a eliminar: ")
    for cliente in utilizadores:
        valores = cliente.values()
        if nome in valores :
            utilizadores.remove(cliente)
    return "Cliente removido"

def adicionar_consumo():
    nome = input("Insira o nome do cliente para adicionar o seu consumo: ")
    for cliente in utilizadores:
        valores = cliente.values()
        if nome in valores:
            consumo_k = "Consumo mensal"
            if len(utilizadores) >= 1:
                consumo_v = int(input("Insira o consumo mensal do cliente: "))
                cliente[consumo_k]=consumo_v
            return "Consumo adicionado"
def chave_consumo(d):
    return d["Consumo mensal"]

def consultar_consumo():
    while True:
        print("1) Consultar um só clientes")
        print("2) Consultar todos os clientes")
        print("3) Voltar atrás")

        funcionalidades = input("Escolha a funcionalidade: ")
        funcionalidades = funcionalidades.strip()
        if funcionalidades == "1":

            nome = input("Insira o nome do cliente para consultar o seu consumo: ")
            for cliente in utilizadores:
                valores = cliente.values()
                if nome in valores:
                    return"O consumo mensal do cliente "+ cliente["Nome do cliente"]+ " é "+ cliente["Consumo mensal"]

        elif funcionalidades == "2":
            return sorted(utilizadores,key=chave_consumo,reverse=True)


def eliminar_consumo():
    nome = input("Insira o nome do cliente para eliminar o seu consumo: ")
    for cliente in utilizadores:
        valores = cliente.values()
        if nome in valores:
            cliente.pop("Consumo mensal")
    return "Consumo removido"

def custo_mensal():
    nome = input("Insira o nome do cliente para consultar o custo mensal e o consumo: ")
    utilizador = {}
    for cliente in utilizadores:
        valores = cliente.values()
        if nome in valores:
            customensal = "Custo mensal"
            if cliente["Existe tarifa social"] == "Sem":
                if ((cliente["Consumo mensal"]) >= 0 and (cliente["Consumo mensal"] <= 5)):
                    preco_metro3 = 0.7354
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):
                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"
                elif ((cliente["Consumo mensal"]) >= 6 and (cliente["Consumo mensal"] <= 15)):
                    preco_metro3 = 1.0509
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):
                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"
                elif ((cliente["Consumo mensal"]) >= 16 and (cliente["Consumo mensal"] <= 25)):
                    preco_metro3 = 2.0859
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):
                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"
                elif cliente["Consumo mensal"]> 25:
                    preco_metro3 = 2.6059
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador
                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):

                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"
            elif cliente["Existe tarifa social"] == "Com":
                if ((cliente["Consumo mensal"]) >= 0 and (cliente["Consumo mensal"] <= 15)):
                    preco_metro3 = 0.7354
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):
                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"
                elif ((cliente["Consumo mensal"]) >= 16 and (cliente["Consumo mensal"] <= 25)):
                    preco_metro3 = 2.0859
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):
                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"
                elif cliente["Consumo mensal"]> 25:
                    preco_metro3 = 2.6059
                    if cliente["Calibre"] <= 25:
                        preco_mensal = 4.8385
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 25) and (cliente["Calibre"] <= 30)):
                        preco_mensal = 19.5959
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 30) and (cliente["Calibre"] <= 50)):
                        preco_mensal = 41.1514
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    elif ((cliente["Calibre"] > 50) and (cliente["Calibre"] <= 100)):
                        preco_mensal = 111.9318
                        cliente[customensal] = preco_metro3 + preco_mensal
                        utilizador["Consumo mensal"] = cliente["Consumo mensal"]
                        utilizador["Custo mensal"] = cliente["Custo mensal"]
                        return utilizador

                    else:
                        return "Calibre errado"




def consultar_escalao():
    print("1) Consultar clientes do 1º escalão")
    print("2) Consultar clientes do 2º escalão")
    print("3) Consultar clientes do 3º escalão")
    print("4) Consultar clientes do 4º escalão")

    funcionalidades = input("Escolha a funcionalidade: ")
    funcionalidades = funcionalidades.strip()
    primeiro_escalao_S = []
    segundo_escalao_S = []
    terceiro_escalao_S = []
    quarto_escalao_S = []

    for cliente in utilizadores:
        if cliente["Existe tarifa social"] == "Sem":
            if ((cliente["Consumo mensal"]) >= 0 and (cliente["Consumo mensal"] <= 5)):
                primeiro_escalao_S.append(cliente)
            elif ((cliente["Consumo mensal"]) >= 6 and (cliente["Consumo mensal"] <= 15)):
                segundo_escalao_S.append(cliente)
            elif ((cliente["Consumo mensal"]) >= 16 and (cliente["Consumo mensal"] <= 25)):
                terceiro_escalao_S.append(cliente)
            elif cliente["Consumo mensal"] > 26:
                quarto_escalao_S.append(cliente)
        elif cliente["Existe tarifa social"] == "Com":
            if ((cliente["Consumo mensal"]) >= 0 and (cliente["Consumo mensal"] <= 15)):
                primeiro_escalao_S.append(cliente)
            elif ((cliente["Consumo mensal"]) >= 16 and (cliente["Consumo mensal"] <= 25)):
                segundo_escalao_S.append(cliente)
            elif cliente["Consumo mensal"] > 26:
                terceiro_escalao_S.append(cliente)

    if funcionalidades == "1":
        return primeiro_escalao_S
    elif funcionalidades == "2":
        return segundo_escalao_S
    elif funcionalidades == "3":
        return  terceiro_escalao_S
    elif funcionalidades == "4":
        return quarto_escalao_S
    else:
        return "Opção invalida. Tente outra funcionalidade"



def main():
    while True:

        print("1) Inserir cliente")
        print("2) Consultar cliente")
        print("3) Eliminar cliente")
        print("4) Adicionar consumo do cliente (mensal)")
        print("5) Consultar consumos")
        print("6) Eliminar consumo do cliente (mensal)")
        print("7) Consultar custo mensal e consumo do cliente")
        print("8) Consultar escalões")
        print("9) Carregar dados")
        print("10) Guardar dados")
        print("11) Apagar dados")
        print("12) Sair")

        funcionalidades = input("Escolha a funcionalidade: ")

        #Remover espaços em branco no inicio e final da string

        funcionalidades = funcionalidades.strip()

        if (funcionalidades == "1"):
            print(inserir_cliente())
        elif (funcionalidades == "2"):
            print(consultar_cliente())
        elif (funcionalidades == "3"):
            print(eliminar_cliente())
        elif(funcionalidades == "4"):
            print(adicionar_consumo())
        elif (funcionalidades == "5"):
            print(consultar_consumo())
        elif (funcionalidades == "6"):
            print(eliminar_consumo())
        elif (funcionalidades == "7"):
            print(custo_mensal())
        elif (funcionalidades == "8"):
            print(consultar_escalao())
        elif(funcionalidades == "9"):
            print(carregar_dados())
        elif(funcionalidades == "10"):
            print(guardar_dados())
        elif(funcionalidades == "11"):
            print(apagar_dados())
        elif (funcionalidades == "12"):
            exit()
        else:
            print("Opção invalida. Tente outra funcionalidade")

print(main())