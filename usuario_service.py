class Usuario:
    def __init__(self, id, login, senha, perfil):
        self.id = id
        self.login = login
        self.senha = senha
        self.perfil = perfil




class UsuarioService:
    def __init__(self):
        self.lista = []
        self.proximo_id = 1


        # ---- Usuário inicial (comente se não quiser) ----
        self.adicionar("admin", "123", "ADMIN")
        # -------------------------------------------------


    def adicionar(self, login, senha, perfil):
        self._validar_dados(login, senha, perfil)


        id = self.proximo_id
        usuario = Usuario(id, login, senha, perfil)
        self.lista.append(usuario)
        self.proximo_id += 1


    def listar(self):
        return self.lista


    def buscar_por_id(self, id):
        for usuario in self.lista:
            if usuario.id == id:
                return usuario
        return None


    def atualizar(self, id, login, senha, perfil):
        self._validar_dados(login, senha, perfil, id)
        usuario = self.buscar_por_id(id)
        if usuario:
            usuario.login = login
            usuario.senha = senha
            usuario.perfil = perfil


    def remover(self, id):
        for usuario in self.lista:
            if usuario.id == id:
                self.lista.remove(usuario)
                break


    def autenticar(self, login, senha):
        for usuario in self.lista:
            if usuario.login == login and usuario.senha == senha:
                return usuario
        raise Exception("Usuário e/ou senha inválidos!")
    


    def _validar_dados(self, login, senha, perfil, id=None):
        if not login or not senha or not perfil:
            raise Exception("Login, senha e perfil são obrigatórios")


        for usuario in self.lista:
            if usuario.login == login:
                # id is None -> método adicionar
                # usuario.id != id -> ignora o próprio usuário no atualizar
                if id is None or usuario.id != id:
                    raise Exception("Login já existe")
