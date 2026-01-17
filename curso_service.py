# curso_service.py


class Curso:
    def __init__(self, id, nome, nivel):
        self.id = id
        self.nome = nome
        self.nivel = nivel




class CursoService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

    def adicionar(self, nome, nivel):
        self._validar_dados(nome, nivel)
        id = self.proximo_id
        curso = Curso(id, nome, nivel)
        self.lista.append(curso)
        self.proximo_id += 1

    
    def buscar_por_id(self, id):
        for curso in self.lista: # percorre todos os alunos da lista
            if curso.id == id:   # verifica se o ID bate com o que foi passado
                return curso     # encontrou → retorna o aluno
        return None 
    
    def listar(self):
        return self.lista
    
    def atualizar (self, id, nome, nivel):
        self._validar_dados(nome, nivel, id)
        curso = self.buscar_por_id(id)
        if curso:
            curso.nome = nome
            curso.nivel = nivel
            
    def remover(self, id):
        for aluno in self.lista:
            if aluno.id == id:
                self.lista.remove(aluno)
                break

    def _validar_dados(self, nome, nivel, id=None):
        if not nome or not nivel:
            raise Exception("Nome e nivel são obrigatórios")


        for curso in self.lista:
            if curso.nivel == nivel:
                # id is None -> referente ao método adicionar
                # aluno.id != id -> desconsidera se aluno for o mesmo que está sendo alterado
                if id is None or curso.id != id:
                    raise Exception("Nivel já existe")