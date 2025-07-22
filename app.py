# app.py (Com feature de lista)
todos = []

def add_task(task):
    todos.append(task)
    print(f"Tarefa adicionada: {task}")

def main():
    print("Bem-vindo ao Sistema de To-Do!")
    add_task("Estudar Git")

if __name__ == "__main__":
    main()