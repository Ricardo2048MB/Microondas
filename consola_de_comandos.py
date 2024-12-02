import cmd
import time

class Microondas(cmd.Cmd):
    intro = 'Bienvenido al microondas. Escribe "help" para ver los comandos disponibles.'
    prompt = '(microondas) '

    def do_calentar(self, line):
        "Calienta la comida por el tiempo especificado en segundos."
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
            print("¡Comida lista!")
        except ValueError:
            print("Por favor, ingresa un número entero para el tiempo.")

    def do_descongelar(self, line):
        "Descongela la comida por el tiempo especificado en minutos."
        try:
            tiempo = int(line)
            print(f"Descongelando por {tiempo} minutos...")
            # Aquí podrías agregar lógica para simular el descongelamiento
            print("¡Comida descongelada!")
        except ValueError:
            print("Por favor, ingresa un número entero para el tiempo.")

    def do_salir(self, line):
        "Sale del programa."
        return True

if __name__ == '__main__':
    Microondas().cmdloop()