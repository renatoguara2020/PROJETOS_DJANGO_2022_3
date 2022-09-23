
class Pessoa:

    def __init__(self, nome, idade, job):
        self.nome = nome
        self.idade = idade
        self.job = job

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setJob(self, job):
        self.job = job

    def getJob(self):
        return self.job
