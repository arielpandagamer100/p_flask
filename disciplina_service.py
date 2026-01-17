# disciplina_service.py


class Disciplina:
    def __init__(self, id, nome, carga_horaria, ementa):
        self.id = id
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.ementa = ementa




class DisciplinaService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1

    def adicionar(self, nome, carga_horaria, ementa):
        self._validar_dados(nome, carga_horaria, ementa)
        id = self.proximo_id
        disciplina = Disciplina(id, nome, carga_horaria, ementa)
        self.lista.append(disciplina)
        self.proximo_id += 1

    
    def buscar_por_id(self, id):
        for disciplina in self.lista: # percorre todos os alunos da lista
            if disciplina.id == id:   # verifica se o ID bate com o que foi passado
                return disciplina     # encontrou → retorna o aluno
        return None 
    
    def listar(self):
        return self.lista
    
    def atualizar (self, id, nome, carga_horaria, ementa):
        self._validar_dados(nome, carga_horaria, ementa, id)
        disciplina = self.buscar_por_id(id)
        if disciplina:
            disciplina.nome = nome
            disciplina.carga_horaria = carga_horaria
            disciplina.ementa = ementa
            
    def remover(self, id):
        for disciplina in self.lista:
            if disciplina.id == id:
                self.lista.remove(disciplina)
                break

    def _validar_dados(self, nome, carga_horaria, id=None):
        if not nome or not carga_horaria:
            raise Exception("Nome e Carga horaria são obrigatórios")


        for disciplina in self.lista:
            if disciplina.carga_horaria == carga_horaria:
                # id is None -> referente ao método adicionar
                # aluno.id != id -> desconsidera se aluno for o mesmo que está sendo alterado
                if id is None or disciplina.id != id:
                    raise Exception("disciplina já existe")