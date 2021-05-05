#CADASTRO DE CLIENTES (NOME, TELEFONE, IDADE)
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDBRevisao"]
mycol = mydb["clientes"]

while True:
    opcao = input("Opções\nA-Inserir\nB-Carregar Dados\nC-Gerar Arquivo\nD-Sair  : ")
    if (opcao == "A"):
        nome = input("NOME: ")
        telefone = input("TELEFONE: ")
        idade = input("IDADE: ")
        mydict = {"nome": nome, "telefone": telefone, "idade": idade}
        mycol.insert_one(mydict)
        print("Registro Inserido!")
    if (opcao == "B"):
        arquivo = open('c:\\tmp\\Clientes.csv', 'r')
        lines = arquivo.readlines()
        for l in lines:
            coluna = l.split(';')
            mydict = {"nome": coluna[0].strip(), "telefone": coluna[1].strip(), "idade": coluna[2].strip()}
            mycol.insert_one(mydict)
        print("Registros carregados na base de dados")
    if (opcao == "C"):
        lstClientes = mycol.find()
        arquivoOutPut = open('c:\\tmp\\ClientesOutPut.txt', 'w')
        clientes = []
        for c in lstClientes:
            clientes.append(c['nome'] + ";" + c['telefone'] + ";" + c['idade'] + "\n")
        arquivoOutPut.writelines(clientes)
        arquivoOutPut.close()
        print("Arquivo gerado com sucesso!")
    if (opcao == "D"):
        break
