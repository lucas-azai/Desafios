class Bicicleta:
    def __init__ (self,cor,modelo,ano,valor):
        self.cor=cor
        self.modelo=modelo
        self.ano=ano
        self.valor=valor
        


    def buzinar (self):
        print ("plim plim")
        
    def parar (self):
        print ("bicicleta parada")
        
    def correr (self):
        print ("correndo")

    def __str__(self):
            return f"Bicicleta: cor={self.cor} Modelo={self.modelo} Ano={self.ano}"

b1 =Bicicleta ("vermelha","caloi",2022,600)
b1.buzinar()
b1.correr()
        
    
    

     