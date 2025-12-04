# main.py
from grade_manager import GradeManager

def main():
    gm = GradeManager()
    gm.load_from_file()

    while True:
        print("\n===== Student Grade Manager =====")
        print("1. Add Student")
        print("2. Update Scores")
        print("3. View Report")
        print("4. Delete Student")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            sid = gm.add_student(name)
            print(f"Student added with ID: {sid}")

            while True:
                sub = input("Enter subject (or 'done'): ")
                if sub.lower() == "done":
                    break
                score = int(input("Score: "))
                gm.update_scores(sid, sub, score)

        elif choice == "2":
            sid = input("Enter student ID: ")
            sub = input("Enter subject: ")
            score = int(input("Enter score: "))
            try:
                gm.update_scores(sid, sub, score)
                print("Score updated.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            sid = input("Enter student ID: ")
            try:
                gm.view_report(sid)
            except ValueError as e:
                print(e)

        elif choice == "4":
            sid = input("Enter student ID: ")
            gm.delete_student(sid)
            print("Student deleted if existed.")

        elif choice == "5":
            gm.save_to_file()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
