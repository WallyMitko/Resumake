import tkinter as tk
import tkinter.ttk as ttk
from src.entry import *


class NewEntryForm(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.form_title = ttk.Label(self, text="New Entry")
        self.form_title.grid(column=2, row=1)

        self.category_label = ttk.Label(self, text="Category")
        self.category_label.grid(column=1, row=2, sticky="E")

        self.category_dropdown = ttk.Combobox(self, state="readonly", values=[e.value for e in EntryCategory])
        self.category_dropdown.set(EntryCategory.WORK.value)
        self.category_dropdown.grid(column=2, row=2, columnspan=2, sticky="W")

        self.title_label = ttk.Label(self, text="Title")
        self.title_label.grid(column=1, row=3, sticky="E")

        self.title_entry = ttk.Entry(self, width=30)
        self.title_entry.grid(column=2, row=3, columnspan=2, sticky="W")

        self.subtitle_label = ttk.Label(self, text="Subtitle")
        self.subtitle_label.grid(column=1, row=4, sticky="E")

        self.subtitle_entry = ttk.Entry(self, width=30)
        self.subtitle_entry.grid(column=2, row=4, columnspan=2, sticky="W")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
