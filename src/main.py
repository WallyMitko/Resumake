import tkinter as tk
import tkinter.ttk as ttk
from src.new_entry_form import NewEntryForm


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.entry_form = NewEntryForm(self)
        self.entry_form.grid(column=1, row=1, sticky="EW")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Resumake")
    main_window = MainApplication(root, padding="3 3 12 12")
    main_window.grid(column=0, row=0, sticky="NEWS")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
