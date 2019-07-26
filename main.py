import random

class Fila(object):
#    """Clase base de fila"""
    def __init__(self):
#         """constructor de la clase Fila """
        self.enfila = 0
        self.fila = []
        
class FilaGeneral(Fila):
#    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
#        """Inserta un nuevo cliente en la fila no preferencial"""
     if cliente.categoria == "general" : 
           self.fila.append(cliente)        
           self.enfila += 1 
     else :
           print("contestame ")        
    def atender(self):
#        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)

class cliente(object):
#     """clase cliente """
    def __init__(self,dni):                                 # metodo constructor
#         """ constructor de la clase cliente """
        self.dni=dni
        self.categoria="general"
    def modificarcategoria(self, categoria):
#        """modifica el atributo categoria del cliente """
        self.categoria = categoria
    def __str__(self) :                                     # Metodo para definir como se imprime el cliente
          return str(self.dni)                              #

class FilaPreferencial(Fila):
#    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
#        """Inserta un nuevo cliente en la fila preferencial"""
##        self.fila.append(cliente) 
     if cliente.categoria == "preferencial":
        self.fila.append(cliente)  
        self.enfila += 1
     else :
        print("por pobre")  

    def atender(self):
#        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
#        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
     if self.enfila > maxenfila : 
         ###filanueva.insertar(self.fila.pop(-1)) 
         extras = self.sel_extras(maxenfila) 
         for c in extras :
            filanueva.insertar(c) 
         
    def sel_extras(self,maxenfila) :
        extra = self.fila[maxenfila:]
        self.fila=self.fila[:maxenfila]
        self.enfila=len(self.fila) 
        return extra
    
    
if __name__ == "__main__":
#    """ simular una fila en una entidad bancaria"

     clientesmaximosdebanco=100
     maxdprefpfil=10
     clientes= []                                       #lista clientes vacia
     filapreferencial = FilaPreferencial()              #colas creadas
     filageneral = FilaGeneral()
     filapreferencial_e = FilaPreferencial()
     for i in range(clientesmaximosdebanco):            #clientes generados y añadidos a la lista 
        clientes.append(cliente(i))             
     for c in clientes :                                  #asginacion de categioria de clietnes  y agragar en las colas correspondientes
        if random.randint(0,100) < 50 :
            c.modificarcategoria("preferencial")
            filapreferencial.insertar(c)
            if filapreferencial.enfila > maxdprefpfil : 
                filapreferencial.abrircajanueva(maxdprefpfil,filapreferencial_e) 
        else :
            filageneral.insertar(c)                                                        
     print(filageneral.enfila, filapreferencial.enfila, filapreferencial_e.enfila)
     filageneral.atender()
     filapreferencial.atender()
     filapreferencial_e.atender()
     print(filageneral.enfila, filapreferencial.enfila, filapreferencial_e.enfila)
     
            


##if ( len(filageneral) > maxdprefpfil ) : 
            
     
     #for c in clientes :
         #print(c.categoria,c.dni)
        
        
     #pepe = cliente(1)
     #pepe.modificarcategoria("general") 
     #filageneral = FilaGeneral()
     #filapreferencial = FilaPreferencial()
     #filapreferencial.insertar(pepe)
     #filageneral.insertar(pepe)
     #print(str(pepe)) 
     #print (*filageneral.fila) 
