import tkinter as tk
import tkinter.ttk as ttk
from entry_info_form import EntryInfoForm
from entry_points_form import EntryPointsForm


class NewEntryForm(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.form_title = ttk.Label(self, text="New Entry")
        self.form_title.grid(column=1, row=1, sticky="SEW")

        self.entry_info_form = EntryInfoForm(self)
        self.entry_info_form.grid(column=1, row=2, sticky="EW")

        self.entry_points_form = EntryPointsForm(self)
        self.entry_points_form.grid(column=1, row=3, sticky="NEW")
