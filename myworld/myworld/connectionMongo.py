import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
meu_banco = cliente['banco_de_dados']
colecao = meu_banco['cientistas']


for itens in colecao.find():
    print(itens)
