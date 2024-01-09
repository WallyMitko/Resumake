import tkinter as tk
import tkinter.ttk as ttk
from entry import BulletPoint


class EntryPointsForm(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.points = [BulletPoint(body="", tags=[])]
        self.point_forms = []

        self.section_title = ttk.Label(self, text="Bullet Points")
        self.section_title.grid(column=1, row=1, sticky="SEW")

        # todo: Load bullet points from persistent storage
        current_point = 0
        for point in self.points:
            point_form = BulletPointForm(self, point, lambda: self.remove_point(point))
            self.point_forms.append(point_form)
            point_form.grid(column=1, row=current_point + 2, sticky="EW")
            current_point += 1

        self.add_button = ttk.Button(self, text="Add", command=self.add_point)
        self.add_button.grid(column=1, row=current_point + 3, sticky="N")

    def remove_point(self, point):
        for form in self.point_forms:
            if form.point == point:
                form.grid_remove()
                self.point_forms.remove(form)
                break
        self.points.remove(point)
        self.update_forms()

    def add_point(self):
        new_point = BulletPoint(body="", tags=[])
        self.points.append(new_point)
        self.point_forms.append(BulletPointForm(self, point=new_point, remove=lambda: self.remove_point(new_point)))
        self.update_forms()

    def update_forms(self):
        current_row = 0
        for i in range(len(self.point_forms)):
            current_row = i + 2
            self.point_forms[i].grid(column=1, row=current_row, sticky="EW")
        if current_row == 0:
            current_row = 2
        self.add_button.grid(column=1, row=current_row + 1)


class BulletPointForm(ttk.Frame):
    def __init__(self, parent, point: BulletPoint, remove, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.point = point
        self.remove = remove

        self.body = tk.StringVar(value=point.body)
        self.joinedTags = ""
        for tag in point.tags:
            self.joinedTags += tag + ", "
        self.tags = tk.StringVar(value=self.joinedTags.rstrip(", "))

        self.body_entry = ttk.Entry(self, textvariable=self.body)
        self.body_entry.grid(column=1, row=1, sticky="E")

        self.tags_entry = ttk.Entry(self, textvariable=self.tags)
        self.tags_entry.grid(column=2, row=1, sticky="EW")

        self.remove_button = ttk.Button(self, text="Remove", command=self.remove)
        self.remove_button.grid(column=3, row=1, sticky="W")
