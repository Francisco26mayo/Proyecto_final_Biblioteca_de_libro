class Libro:
    def __init__(self, autor, titulo, editorial):
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
 
    @property
    def autor(self):
        return self._autor
 
    @autor.setter
    def autor(self, autor):
        self._autor = autor
 
    @property
    def titulo(self):
        return self._titulo
 
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
 
    @property
    def editorial(self):
        return self._editorial
 
    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial