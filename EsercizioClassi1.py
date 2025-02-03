class Punto:
    x = 0
    y = 0
    
    def muovi(self, nuovox, nuovoy):
        self.x = nuovox
        self.y = nuovoy
        
    def distana_da_origine(self):
        return (self.x**2 + self.y**2) **0.5
        
    
p = Punto()
print(p.x, p.y)  
p.muovi(2, 3)
print (p.x, p.y)
print(p.distana_da_origine())