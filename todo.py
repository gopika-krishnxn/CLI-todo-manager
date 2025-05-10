import os

todo_file = "tasks.txt"

def show_tasks():
    if not os.path.exists(todo_file) or os.path.getsize(todo_file) == 0:
        print("\n📭 No tasks found.")
        return
    with open(todo_file, "r") as file:
        tasks = file.readlines()
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def add_task():
    task = input("📝 Enter new task: ").strip()
    if task:
        with open(todo_file, "a") as file:
            file.write(task + "\n")
        print("✅ Task added.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("❌ Enter task number to delete: "))
        with open(todo_file, "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open(todo_file, "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Removed: {removed.strip()}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
