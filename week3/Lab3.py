import datetime
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\033[92m'
star = '*'*10


class Note:
    ID_count = 1

    def __init__(self, memo, tags):
        self.memo = memo
        self._creation_date = datetime.date.today()
        self._tags = tags
        self._ID = Note.ID_count

        Note.ID_count += 1

    def match(self, search_filter):
        return search_filter in self.memo or search_filter in self.tag
    
    @property
    def creation_date(self):
        return self._creation_date
    
    @property
    def tag(self):
        return self._tags
    
    @property
    def ID(self):
        return self._ID

    @tag.setter
    def tag(self, value):
        self._tags=value


class Notebook:
    def __init__(self):
        self.notes = []
    

    def new_note(self, memo, tags):
        if isinstance(memo, str) and isinstance(tags, list):
            self.notes.append(Note(memo, tags))
            Menu.green_print("Note added successfully")
        else:
            Menu.red_print("Memo and tags must be string")

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.ID == note_id:
                note.memo = memo
                self.success_edit(note)
                break
        else:
            Menu.red_print("No note with that id")

    def modify_tags(self, note_id, tags):
        if isinstance(tags, list):
            for note in self.notes:
                if note.ID == note_id:
                    note.tag = tags
                    self.success_edit(note)
                    break
            else:
                Menu.red_print("No note with that id")

    def search_notes(self, filter):
        if isinstance(filter, str):
            counter=0
            print("*" * 10)
            for note in self.notes:
                if note.match(filter):
                    print(f"Note ID : {note.ID}")
                else:
                    counter += 1
                if counter == len(self.notes):
                    Menu.red_print("No notes found")

        else:
            Menu.red_print("Filter must be string")

    def success_edit(self, note):
        print("\n"+("*" * 10)+"\n")
        Menu.green_print("Note modified successfully")
        print(f"Note ID : {note.ID}")
        print(f"Memo : {note.memo}")
        print(f"Tags : {note.tag}\n")



class Menu:
    def __init__(self):
        self.notebook = Notebook()
    def show_note(self, note_id):
        note_id,check=self.change_str_toint(note_id)
        if check:
            for note in self.notebook.notes:
                if note.ID == note_id:
                    print("*" * 5)
                    print(f"\nNote ID : {note.ID}")
                    print(f"Timestamp : {note.creation_date}")
                    print(f"Memo : {note.memo}")
                    print(f"Tags : {note.tag}\n")
                    print("*" * 5)
                    break
            else:
                Menu.red_print("No note with that id")

    def search_note(self, value):
        self.notebook.search_notes(value)

    def add_note(self, memo, tags):
        self.notebook.new_note(memo, tags)

    def modify_note(self, note_id, memo):
        self.notebook.modify_memo(note_id, memo)

    def modify_tags(self, note_id, tags):
        self.notebook.modify_tags(note_id, tags)
    def quit(self):
        print("Ok, goodbye")
        exit()

    @staticmethod
    def change_str_toint(value):
        if value.isnumeric():
            return int(value),True
        else:
            Menu.red_print(star+"ID must be Number"+star)
            return value,False

    @staticmethod
    def red_print(value):
        print(CRED+value+CEND)

    @staticmethod
    def green_print(value):
        print(CGREEN+value+CEND)
# loop use class menu to run
menu = Menu()
menu.add_note("first note", ["first", "test"])
menu.add_note("second note", ["second", "test"])
print("add sample note")
while True:
    print(
        """
    Notebook Menu
    1. Show Note
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Modify Tags
    6. Quit
    """
    )
    select = input("Enter your choice: ")
    match select:
        case "1":
            menu.show_note(input("Enter note id: "))
        case "2":
            menu.search_note(input("Enter search filter: "))
        case "3":
            print("**********Use spacebar when you need to more than 1 tags**********")

            menu.add_note(input("Enter memo: "), input("Enter tags: ").split())
        case "4":
            note_id=input("Enter note id: ")
            note_id,check=menu.change_str_toint(note_id)
            if check:
                menu.modify_note(note_id, input("Enter memo: "))
        case "5":
            print("**********Use spacebar when you need to more than 1 tags**********")
            note_id=input("Enter note id: ")
            note_id,check=menu.change_str_toint(note_id)
            if check:
                menu.modify_tags(note_id, input("Enter tags: ").split())
        case "6":
            menu.quit()
        case _:
            print("**********Your selection is not in Menu***********")
