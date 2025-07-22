# app.py (Versão inicial)
def main():
    print("Bem-vindo ao Sistema de To-Do!")

def add_task(task, todos=None):
    if not task:
        print("Erro: Tarefa vazia!")  # Correção do bug
    else:
        todos.append(task)
        print(f"Tarefa adicionada: {task}")

if __name__ == "__main__":
    main()