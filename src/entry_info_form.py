import tkinter as tk
import tkinter.ttk as ttk
from entry import *
from datetime import date


class EntryInfoForm(ttk.Frame):
    MONTHS = {
        "<None>": 0,
        "January": 31,
        "February": 0,  # handled separately due to leap years
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    def days_in_month(self, month: str, year: int) -> int:
        if month != "February":
            return self.MONTHS[month]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.title = tk.StringVar(value="")
        self.subtitle = tk.StringVar(value="")
        self.category = tk.StringVar(value=EntryCategory.WORK.value)
        self.start_year = tk.IntVar(value=date.today().year)
        self.start_month = tk.StringVar(value=list(self.MONTHS)[0])
        self.start_day = tk.IntVar(value=0)
        self.end_year = tk.IntVar(value=date.today().year)
        self.end_month = tk.StringVar(value=list(self.MONTHS)[0])
        self.end_day = tk.IntVar(value=0)
        self.is_ongoing = tk.BooleanVar(value=False)

        self.category_label = ttk.Label(self, text="Category")
        self.category_label.grid(column=1, row=2, sticky="E")

        self.category_dropdown = ttk.Combobox(self, state="readonly", values=[e.value for e in EntryCategory])
        self.category_dropdown.set(EntryCategory.WORK.value)
        self.category_dropdown.grid(column=2, row=2, columnspan=2, sticky="W")

        self.title_label = ttk.Label(self, text="Title")
        self.title_label.grid(column=1, row=3, sticky="E")

        self.title_entry = ttk.Entry(self, width=30, textvariable=self.title)
        self.title_entry.grid(column=2, row=3, columnspan=2, sticky="W")

        self.subtitle_label = ttk.Label(self, text="Subtitle")
        self.subtitle_label.grid(column=1, row=4, sticky="E")

        self.subtitle_entry = ttk.Entry(self, width=30, textvariable=self.subtitle)
        self.subtitle_entry.grid(column=2, row=4, columnspan=2, sticky="W")

        # Start date
        self.start_date_label = ttk.Label(self, text="Start Date")
        self.start_date_label.grid(column=1, row=5, sticky="E")

        self.start_year_spinner = ttk.Spinbox(self, from_=1900, to=2100, textvariable=self.start_year)
        self.start_year_spinner.grid(column=2, row=5, sticky="WE")

        self.start_month_dropdown = ttk.Combobox(
            self,
            state="readonly",
            values=list(self.MONTHS),
            textvariable=self.start_month
        )
        self.start_month_dropdown.grid(column=3, row=5, sticky="WE")

        self.start_day_spinner = ttk.Spinbox(self, from_=1, to=1, textvariable=self.start_day, state="disabled")
        self.start_day_spinner.grid(column=4, row=5, sticky="W")
        self.start_month_dropdown.bind("<<ComboboxSelected>>", self.update_start_days)

        # End date
        self.end_date_label = ttk.Label(self, text="End Date")
        self.end_date_label.grid(column=1, row=6, sticky="E")

        self.end_year_spinner = ttk.Spinbox(self, from_=1900, to=date.today().year, textvariable=self.end_year)
        self.end_year_spinner.grid(column=2, row=6, sticky="WE")

        self.end_month_dropdown = ttk.Combobox(
            self,
            state="readonly",
            values=list(self.MONTHS),
            textvariable=self.end_month
        )
        self.end_month_dropdown.grid(column=3, row=6, sticky="WE")

        self.end_day_spinner = ttk.Spinbox(self, from_=1, to=1, textvariable=self.end_day, state="disabled")
        self.end_day_spinner.grid(column=4, row=6, sticky="WE")
        self.end_month_dropdown.bind("<<ComboboxSelected>>", self.update_end_days)

        self.ongoing_checkbox = ttk.Checkbutton(
            self,
            text="Ongoing",
            variable=self.is_ongoing,
            command=self.update_ongoing
        )
        self.ongoing_checkbox.grid(column=5, row=6, sticky="W")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def update_start_days(self, e):
        current_start_day = self.start_day.get()
        new_days_in_month = self.days_in_month(self.start_month.get(), self.start_year.get())
        self.start_day_spinner.configure(to=new_days_in_month)
        self.start_day.set(min(current_start_day, new_days_in_month))
        if new_days_in_month == 0:
            self.start_day_spinner.state(['disabled'])
        else:
            self.start_day_spinner.state(['!disabled'])

    def update_end_days(self, e):
        current_end_day = self.end_day.get()
        new_days_in_month = self.days_in_month(self.end_month.get(), self.end_year.get())
        self.end_day_spinner.configure(to=new_days_in_month)
        self.end_day.set(min(current_end_day, new_days_in_month))
        if new_days_in_month == 0:
            self.end_day_spinner.state(['disabled'])
        else:
            self.end_day_spinner.state(['!disabled'])

    def update_ongoing(self):
        if self.is_ongoing.get():
            self.end_year_spinner.state(["disabled"])
            self.end_month_dropdown.state(["disabled"])
            self.end_day_spinner.state(["disabled"])
        else:
            self.end_year_spinner.state(["!disabled"])
            self.end_month_dropdown.state(["!disabled"])
            self.end_day_spinner.state(["!disabled"])
