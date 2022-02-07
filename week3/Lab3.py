import datetime
class Note():
    ID_count = 1
    def __init__(self, memo, tags):
        self.memo = memo
        self._creation_date =  datetime.date.today()
        self._tags = tags
        self._ID = Note.ID_count
        
        Note.ID_count += 1
        
    def match(self,search_filter):
        return search_filter in self.memo or search_filter in self._tags
        

class Notebook():
    def __init__(self):
        self.notes = []
    def new_note(self, memo, tags):
        if isinstance(memo,str) and isinstance(tags,list):
            self.notes.append(Note(memo,tags))
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
        if isinstance(tags,list):
            for note in self.notes:
                if note._ID == note_id:
                    note._tags = tags
                    break
            else:
                print("no note with that id")
    def search_notes(self, filter):
        if isinstance(filter,str):
            for note in self.notes:
                if note.match(filter):
                    print(f"note id: {note._ID} memo: {note.memo} tags: {note._tags} creation_date: {note._creation_date}")
        else:
            print("filter is not a string")
class Menu():
        def ___init__(self):
            self.notebook = Notebook()
        
        def show_note(self):
            for note in self.notebook.notes:
                print(f"note id: {note._ID} memo: {note.memo} tags: {note._tags} creation_date: {note._creation_date}")

        def search_note(self,value):
            self.notebook.search_notes(value)
        
        def add_note(self,memo, tags):
            self.notebook.new_note(memo,tags)
        
        def modify_note(self, note_id, memo):
            self.notebook.modify_memo(note_id, memo)
        
        def modify_tags(self, note_id, tags):
            self.notebook.modify_tags(note_id, tags)
        