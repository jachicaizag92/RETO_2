# Clase con las operaciones matematicas necesarias y sus respectivos metodos
class CalculadoraSaludable():
    
    def __init__(self,sexo,edad,altura,peso,met,tiempo):
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.met = met
        self.tiempo = tiempo
        
    def pesoIdeal(self):
        if self.sexo =="hombre":
            pesoIdeal = round(56.2+1.41*(self.altura/2.54-60))
            print(f"tu peso ideal es de: {pesoIdeal} Kg\n")
        elif self.sexo == "mujer":
            pesoIdeal = round(53.1+1.36*(self.altura/2.54-60))
            print(f"tu peso ideal es de: {pesoIdeal} Kg\n")
        else:
            print("fuera de los parametros establecidos")
            
    def quemandoCalorias(self):
        if self.met == "caminar":
            self.met = 2
            calorias = round((self.tiempo*self.met*self.peso)/200)
            print(f"Las calorias quemadas caminando son: {calorias} calorias\n")
        elif self.met == "tenis":
            self.met = 5
            calorias = round((self.tiempo*self.met*self.peso)/200)
            print(f"Las calorias quemadas jugando tenis son: {calorias} calorias\n")
        elif self.met == "bicicleta":
            self.met = 14
            calorias = round((self.tiempo*self.met*self.peso)/200)
            print(f"Las calorias quemadas realizando bicicleta son: {calorias} calorias\n")
        elif self.met == "correr":
            self.met = 6
            calorias = round((self.tiempo*self.met*self.peso)/200)
            print(f"Las calorias quemadas corriendo son: {calorias} calorias\n")
        elif self.met == "nadar":
            self.met = 9.8
            calorias = round((self.tiempo*self.met*self.peso)/200)
            print(f"Las calorias quemadas nadando son: {calorias} calorias\n")
        else:
            print("fuera de los parametros establecidos")
            
    def porcentajeGrasaCorporal(self):
        imc = self.peso /(self.altura*0.01)**2
        if self.sexo == "hombre":
            grasaCorporal = round((1.20*imc)+(0.23*self.edad)-16.2)
            print(f"tu porcentaje de grasa corporal es de: {grasaCorporal}% \n")
        elif self.sexo == "mujer":
            grasaCorporal =round((1.20*imc)+(0.23*self.edad)-5.4)
            print(f"tu porcentaje de grasa corporal es de: {grasaCorporal}% \n")
        else:
            print("fuera de los parametros establecidos")
    
    def indicieMetabolicoBasal(self):
        if self.sexo == "hombre":
            indice = round(13.397*(self.peso)+4.799*(self.edad)-5.677*(self.altura)+88.362)
            print(f"Segun tu indice (TMB) necesitas {indice} calorias \n")
        elif self.sexo == "mujer":
            indice = round(9.247*(self.peso)+3.098*(self.edad)-4.330*(self.altura)+447.593)
            print(f"Segun tu indice (TMB) necesitas {indice} calorias \n")
        else:
            print("fuera de los parametros establecidos")

#clase del menu permite seleccionar opcion y validar la informacion recibida y sus respectivos metodos
class Menu():
    
    
    print("************************************************************")
    print("********************CALCULDORA SALUDABLE********************")
    print("************************************************************\n")
    print("Por favor ingrese el genero: ")
    print("seleccione la opcion de su genero")
    print("1. Hombre")
    print("2. Mujer \n")
    genero = int(input())
    print("************************************************************")
    print("Por favor ingrese su edad en años: ")
    edad = int(input())
    print("************************************************************")
    print("Por favor ingrese su altura en centimetros: ")
    altura = int(input())
    print("************************************************************")
    print("Por favor ingrese su peso en kilogramos: ")
    peso = int(input())
    print("************************************************************")
    print("Por favor ingrese su actividad deportiva: ")
    print("seleccione la opcion")
    print("1. Caminar")
    print("2. Tenis")
    print("3. Montar en bicicleta")
    print("4. correr")
    print("5. Nadar\n")
    actividad = int(input())
    print("************************************************************")
    print("Por favor ingrese el tiempo en minutos de la actividad deportiva seleccionada: ")
    tiempoActividad = int(input())
    print("\n************************************************************")
    print("************************************************************")
    print("************************* RESULTADOS ***********************")
    print("************************************************************\n")

        
    def getGenero(self):
        if self.genero == 1:
            return("hombre")
            
        elif self.genero == 2:
            return("mujer")
        else:
            return("no es un genero")
            
    def getEdad(self):
        return self.edad
    
    def getAltura(self):
        return self.altura
    
    def getPeso(self):
        return self.peso
    
    def getActividad(self):
        if self.actividad == 1:
            return("caminar")
        elif self.actividad == 2:
            return("tenis")
        elif self.actividad == 3:
            return("bicicleta")
        elif self.actividad == 4:
            return("correr")
        elif self.actividad == 5:
            return("nadar")
        else:
            return("no es una actividad fisica")
        
    def getTiempoActividad(self):
        return self.tiempoActividad
        




#inicializamos la instancia de la clase Menu
menu = Menu()
#inicializamos la instancia de la clase CalculadoraSaludable y los argumentos por medio de metodos de la clase Menu 
calc = CalculadoraSaludable(menu.getGenero(),menu.getEdad(),menu.getAltura(),menu.getPeso(),menu.getActividad(),menu.getTiempoActividad())
#metodo de la clase CalculadoraSaludable
calc.pesoIdeal()
#metodo de la clase CalculadoraSaludable
calc.quemandoCalorias()
#metodo de la clase CalculadoraSaludable
calc.porcentajeGrasaCorporal()
#metodo de la clase CalculadoraSaludable
calc.indicieMetabolicoBasal()