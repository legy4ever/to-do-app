from colorama import init, Fore
import os

init()

MARK_COMPLETED = '[X]'
TODO_LIST_FILE = 'todolist.txt'


def validar_file():
    if not os.path.exists(TODO_LIST_FILE):
        open(TODO_LIST_FILE, 'w').close()


validar_file()

with open(TODO_LIST_FILE, 'r') as f:
    tareas = f.readlines()


def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


limpiar_terminal()

print(Fore.BLUE + 'Tareas: ')
for i, tarea in enumerate(tareas):
    print(Fore.BLUE + f'{i+1}. {tarea.strip()}')


def error_num_tarea():
    print(Fore.RED + 'Ingrese un número de tarea válido, puede ingresar el comando "l" para listar las tareas y ver los números válidos.' + Fore.RESET)


def error_tarea_completada():
    print(Fore.RED + f'No se puede editar una tarea ya completada.' + Fore.RESET)


def success_tarea_editada(num):
    print(Fore.GREEN +
          f'Tarea "{num}" editada correctamente.' + Fore.RESET)


def success_tarea_eliminada(num):
    print(
        Fore.GREEN + f'Tarea "{num}" eliminada de la lista de tareas.' + Fore.RESET)


def escribir_archivo():
    with open(TODO_LIST_FILE, 'w') as f:
        for tarea in tareas:
            f.write(tarea)


while True:
    comando = input(Fore.YELLOW + 'Ingresa un comando: ' + Fore.RESET)
    if comando == 'a':
        nueva_tarea = input(
            Fore.YELLOW + 'Ingrese una nueva tarea: ' + Fore.RESET)
        tareas.append(f'{nueva_tarea}\n')
        escribir_archivo()
        print(Fore.GREEN +
              f'Tarea "{nueva_tarea}" agregada a la lista de tareas.' + Fore.RESET)
    elif comando == 'e':
        num_tarea = input(
            Fore.YELLOW + 'Ingrese el número de la tarea que desee editar: ' + Fore.RESET)
        try:
            num_tarea = int(num_tarea)
            if len(tareas) >= num_tarea:
                if tareas[num_tarea-1].startswith(MARK_COMPLETED):
                    error_tarea_completada()
                else:
                    tarea_editada = input(
                        Fore.BLUE + f'Ingrese el nuevo valor de la tarea número "{num_tarea}": ' + Fore.RESET)
                    tareas[num_tarea-1] = tareas[num_tarea -
                                                 1].replace(tareas[num_tarea-1], tarea_editada)
                    escribir_archivo()
                    success_tarea_editada(num_tarea)
            else:
                error_num_tarea()
        except:
            error_num_tarea()
    elif comando == 'd':
        num_tarea = input(
            Fore.YELLOW + 'Ingresa el número de la tarea que desea eliminar:' + Fore.RESET)
        try:
            num_tarea = int(num_tarea)
            tarea_eliminada = tareas.pop(num_tarea-1)
            escribir_archivo()
            success_tarea_eliminada(nueva_tarea)
        except (ValueError, IndexError):
            error_num_tarea()
    elif comando == 'c':
        num_tarea = input(
            Fore.YELLOW + 'Ingresa el número de la tarea que desea marcar como completada:')
        try:
            num_tarea = int(num_tarea)
            tareas[num_tarea-1] = tareas[num_tarea -
                                         1].replace(tareas[num_tarea-1], f'{MARK_COMPLETED} {tareas[num_tarea-1]}')
            escribir_archivo()
            print(
                Fore.GREEN + f'Tarea "{num_tarea}" marcada como completada de la lista de tareas.' + Fore.RESET)
        except (ValueError, IndexError):
            error_num_tarea()
    elif comando == 'q':
        print(Fore.BLUE + 'Saliendo del programa...' + Fore.RESET)
        break
    elif comando == 'l':
        print(Fore.BLUE + 'Tareas: ' + Fore.RESET)
        for i, tarea in enumerate(tareas):
            print(Fore.BLUE + f'{i+1}. {tarea.strip()}' + Fore.RESET)
    elif comando == 'clear':
        limpiar_terminal()
    else:
        print(Fore.RED + 'Ingrese un comando válido.' + Fore.RESET)
