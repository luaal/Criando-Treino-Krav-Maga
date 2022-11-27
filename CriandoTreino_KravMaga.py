class Golpe:
    def __init__(self,nome, tipo):
        self.nome = nome.title()
        self.tipo = tipo
    

    def __str__(self):
        return f'Nome: {self.nome} | Tipo: {self.tipo}'


class Beitat(Golpe):
    def __init__(self,nome,tipo, forma):
        super().__init__(nome, tipo)
        self.forma = forma

    @property
    def formas(self):
        return self.formas

    @formas.setter
    def formas(self, formas):
        self.formas = formas

    def __str__(self):
        return f'Nome: {self.nome} | Tipo: {self.tipo} | Forma: {self.forma}'

class Makat(Golpe):
    def __init__(self,nome,tipo, distancia):
        super().__init__(nome, tipo)
        self.distancia = distancia
  
    def __str__(self):
        return f'Nome: {self.nome} | Tipo: {self.tipo} | Distância: {self.distancia}'


class Treino():
    def __init__(self, nome, faixa):
        self.nome = nome
        self._faixa = faixa

    def __getitem__(self,item):
        return self._faixa[item]

    def __len__(self):
        return len(self._faixa)

gilgul = Golpe("Gilgul Lefanim", "rolamento")
smol_yamin = Makat("Smol Yamin", "duro", "longa")
beitat_reguila = Beitat("Beitat Reguila Lefanim", "Regular", "4 movimentos")

treino_faixaBranca = [gilgul, smol_yamin, beitat_reguila]
treino_segundaFeira = Treino("Treino Segunda-feira", treino_faixaBranca)

for treino in treino_segundaFeira:
    print(treino)

print(f"Quantidade de Exercicios: {len(treino_segundaFeira)}")