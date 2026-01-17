# professor_service.py


class Professor:
    def __init__(self, id, nome, cpf, disciplina):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina




class ProfessorService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1


    def adicionar(self, nome, cpf, disciplina):
        self._validar_dados(nome, cpf)
        id = self.proximo_id
        professor = Professor(id, nome, cpf, disciplina)
        self.lista.append(professor)
        self.proximo_id += 1


    def buscar_por_id(self, id):
        for professor in self.lista: # percorre todos os alunos da lista
            if professor.id == id:   # verifica se o ID bate com o que foi passado
                return professor     # encontrou → retorna o aluno
        return None 


    def listar(self):
        return self.lista
    
    def atualizar (self, id, nome, cpf, disciplina):
        self._validar_dados(nome, cpf, id)
        professor = self.buscar_por_id(id)
        if professor:
            professor.nome = nome
            professor.cpf = cpf
            professor.disciplina = disciplina
            
    def remover(self, id):
        for professor in self.lista:
            if professor.id == id:
                self.lista.remove(professor)
                break
    
    
    def _validar_dados(self, nome, cpf, id=None):
        if not nome or not cpf:
            raise Exception("Nome e cpf são obrigatórios")


        for professor in self.lista:
            if professor.cpf == cpf:
                # id is None -> referente ao método adicionar
                # aluno.id != id -> desconsidera se aluno for o mesmo que está sendo alterado
                if id is None or professor.id != id:
                    raise Exception("CPF já existe")