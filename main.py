#Menu actions

add = 1
edit = 2
done = 3
delete = 4
listTask = 5
close = 6
minimumOption = 1
maximumOption = 6


class Task:
    def __init__(self, name, dueDate):
        self.name = name
        self.dueDate = dueDate
        self.done = False

    def printData(self, index):
        print("{0}. Tarea: {1}, Fecha: {2}, Hecha:{3}".format(index, self.name, self.dueDate, self.done))




def printMenu():
    print("*************************")
    print("* EDtodo                *")
    print("*************************")
    print("* Seleccione una opción *")
    print("*************************")
    print("* 1. Agrege una tarea*")
    print("* 2. Editar tarea")
    print("* 3. Marcar como hecha")
    print("* 4. Borrar tarea")
    print("* 5. Listar tareas")
    print("* 6. Salir")



def printTitleList():
    print("")
    print("***********************")
    print("*  LISTADO DE TAREAS  *")
    print("***********************")
    print("")



def getOption():
    try:
        optionStr = input("* Digite la opción: ")
        optionInt= int(optionStr)
    except ValueError:
        print("Este no es un entero, digite solo número enteros.")

    return optionInt



def createTask():
    name = input("Nombre: ")
    dueDate = input("Fecha: ")
    task= Task(name, dueDate)
    return task



def isValidOption(option):
    if option < minimumOption or option > maximumOption:
        return False

    return True



def newList():
    return []



def addTask(task, toDo):
    toDo.append(task)



def processAddTask(toDo):
    print("Crear Tarea")
    task = createTask()
    addTask(task, toDo)
    print("** Tarea Creada **")



def printAllTask(toDo):
    index = 0
    for task in toDo :
        index += 1
        task.printData(index)



def getIndex():
    try:
        value = input("Digite el número de la tarea: ")
        index = int(value)
    except ValueError:
        print("Ese no es un número valido")

    return index



def editTask(index, newTask, toDo):
    toDo[index-1] = newTask



def processEditTask(toDo):
    print("Editar tarea")
    index = getIndex()
    task = createTask()
    editTask(index, task, toDo)
    print("** Tarea Editada **")



def setIsDone():
    value = input("Digite 1 si ya se hizo, de lo contrario cualquier otra tecla: ")
    if value == "1":
        return True

    return False



def doneTask(index, done, toDo):
    toDo[index-1].done = done



def processDoneTask(toDo):
    print("Marcar tarea como hecha")
    index = getIndex()
    done = setIsDone()
    doneTask(index, done,toDo)



def deleteTask(index, toDo):
    del toDo[index-1]



def processDeleteTask(toDo):
    print("Borrar Tarea")
    index = getIndex()
    deleteTask(index, toDo)
    print("Tarea borrada")

def process(option, toDo):
    if option == add:
        processAddTask(toDo)
        return

    if option == edit:
        processEditTask(toDo)
        return

    if option == done:
        processDoneTask(toDo)
        return

    if option == delete:
        processDeleteTask(toDo)
        return

    if option == listTask:
        printTitleList()
        printAllTask(toDo)
        return



def execute():
    option = 0

    toDo = newList()
    while option != close :
        printMenu()
        option = getOption()
        if not isValidOption(option):
            print("Opción no valida, intente con un número del 1 al 6")
            continue

        process(option, toDo)

execute()