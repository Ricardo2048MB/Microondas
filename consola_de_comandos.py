import cmd

class Microondas(cmd.Cmd):
    intro = 'Bienvenido al microondas. Escribe "help" para ver los comandos disponibles.'
    prompt = '(microondas) '

    def do_calentar(self, line):
        "Calienta la comida por el tiempo especificado en segundos."
        try:
            tiempo = int(line)
            print(f"Calentando por {tiempo} segundos...")
            # Aquí podrías agregar lógica para simular el calentamiento
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