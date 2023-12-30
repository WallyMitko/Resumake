import tkinter as tk
import tkinter.ttk as ttk


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # create gui
        self.test_str = tk.StringVar()
        self.test_entry = ttk.Entry(self, width=7, textvariable=self.test_str)
        self.test_entry.grid(column=2, row=1, sticky="WE")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Resumake")
    main_window = MainApplication(root, padding="3 3 12 12")
    main_window.grid(column=0, row=0, sticky="NEWS")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
