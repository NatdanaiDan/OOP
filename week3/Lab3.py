import datetime


class Note:
    ID_count = 1

    def __init__(self, memo, tags):
        self.memo = memo
        self._creation_date = datetime.date.today()
        self._tags = tags
        self._ID = Note.ID_count

        Note.ID_count += 1

    def match(self, search_filter):
        return search_filter in self.memo or search_filter in self._tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags):
        if isinstance(memo, str) and isinstance(tags, list):
            self.notes.append(Note(memo, tags))
        else:
            print("memo and tags must be string and list")

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note._ID == note_id:
                note.memo = memo
                break
        else:
            print("no note with that id")

    def modify_tags(self, note_id, tags):
        if isinstance(tags, list):
            for note in self.notes:
                if note._ID == note_id:
                    note._tags = tags
                    break
            else:
                print("no note with that id")

    def search_notes(self, filter):
        if isinstance(filter, str):
            for note in self.notebook.notes:
                if note.match(filter):
                    print(f"Note : {note._ID}")
        else:
            print("filter must be string")


class Menu:
    def __init__(self):
        self.notebook = Notebook()

    # shownote use id parameter to select note

    def show_note(self, note_id):
        for note in self.notebook.notes:
            if note._ID == note_id:
                print(f"Note ID : {note._ID}")
                print(f"Memo : {note.memo}")
                print(f"Tags : {note._tags}")
                break
        else:
            print("No note with that id")

    def search_note(self, value):
        self.notebook.search_notes(value)

    def add_note(self, memo, tags):
        print(self.notebook)
        self.notebook.new_note(memo, tags)

    def modify_note(self, note_id, memo):
        self.notebook.modify_memo(note_id, memo)

    def modify_tags(self, note_id, tags):
        self.notebook.modify_tags(note_id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        exit()


# loop use class menu to run
menu = Menu()

while True:
    print("""
    Notebook Menu
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Modify Tags
    6. Quit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        menu.show_note(int(input("Enter note id: ")))
    elif choice == "2":
        menu.search_note(input("Enter search filter: "))
    elif choice == "3":
        menu.add_note(input("Enter memo: "), input("Enter tags: ").split(" "))
    elif choice == "4":
        menu.modify_note(int(input("Enter note id: ")), input("Enter memo: "))
    elif choice == "5":
        menu.modify_tags(int(input("Enter note id: ")),
                         input("Enter tags: ").split(" "))
    elif choice == "6":
        menu.quit()
