import cmd
import time

class Microondas(cmd.Cmd):
    intro = 'Bienvenido al microondas. Escribe "help" para ver los comandos disponibles.'
    prompt = '(microondas) '
    
    presets = {
        'palomitas': 3 * 60,  # 3 minutos
        'yakimeshi': 2 * 60 + 30,  # 2 minutos y 30 segundos
        'spaghetti': 1 * 60 + 45  # 1 minuto y 45 segundos
    }

    def do_calentar(self, line):
        """
Calienta la comida por el tiempo especificado en segundos.
        
Sintaxis
        
calentar <segundos | preset>

Presets disponibles: palomitas, yakimeshi, y spaghetti.
        
        """
        if line in self.presets:
            tiempo_segundos = self.presets[line]
            minutos, segundos = divmod(tiempo_segundos, 60)
            alimento = line
            while minutos >= 0 and segundos >= 0:
                print(f"{minutos:02d}:{segundos:02d}", end='\r')  # Imprime y regresa al inicio de la línea
                time.sleep(1)  # Espera 1 segundo
                segundos -= 1
                if segundos < 0:
                    minutos -= 1
                    segundos = 59
            print(f"¡{alimento.capitalize()} listo! Buen provecho.")
        else:
            try:
                tiempo_segundos = int(line)
                minutos, segundos = divmod(tiempo_segundos, 60)
                alimento = input("¿Qué alimento estás calentando? ")
                while minutos >= 0 and segundos >= 0:
                    print(f"{minutos:02d}:{segundos:02d}", end='\r')  # Imprime y regresa al inicio de la línea
                    time.sleep(1)  # Espera 1 segundo
                    segundos -= 1
                    if segundos < 0:
                        minutos -= 1
                        segundos = 59
                print(f"¡{alimento.capitalize()} listo! Buen provecho.")
            except ValueError:
                print("Por favor, ingresa un número entero para el tiempo o el nombre de un preset.")

    def do_descongelar(self, line):
        """
Descongela la comida por el tiempo especificado en segundos.

Sintaxis

descongelar <segundos>
        """
        try:
            tiempo_segundos = int(line)
            minutos, segundos = divmod(tiempo_segundos, 60)
            
            while minutos >= 0 and segundos >= 0:
                print(f"{minutos:02d}:{segundos:02d}", end='\r')  # Imprime y regresa al inicio de la línea
                time.sleep(1)  # Espera 1 segundo
                segundos -= 1
                if segundos < 0:
                    minutos -= 1
                    segundos = 59
            print("¡Comida descongelada!")
        except ValueError:
            print("Por favor, ingresa un número entero para el tiempo.")

    def do_salir(self, line):
        "Sale del programa."
        return True

if __name__ == '__main__':
    Microondas().cmdloop()