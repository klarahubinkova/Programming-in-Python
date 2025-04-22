todos = []

def add_task(task):
    """
    Přidá nový úkol do seznamu úkolů.

    Parametry:
    task (str): Nový úkol, který má být přidán.
    """
    todos.append(task)

def remove_task(task):
    """
    Odstraní zadaný úkol ze seznamu úkolů, pokud existuje.
    Pokud úkol neexistuje, vypíše chybovou zprávu.

    Parametry:
    task (str): Úkol, který má být odstraněn.
    """
    if task in todos:
        todos.remove(task)
    else:
        print(f"'{task}' not in TODO list.")

def view_tasks():
    """
    Vypíše všechny úkoly v seznamu na obrazovku.
    """
    for task in todos:
        print(task)

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        print("Your tasks:")
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
    
    print()
