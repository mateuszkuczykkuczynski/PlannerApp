from tkinter import *
from tkinter import messagebox
import pickle


class MainApplication(Tk):
    def __init__(self):
        super().__init__()

        # Configure the root window
        self.title("Your Daily Planner")
        self.geometry("600x800")
        self.config(bg="gray85")
        self.resizable(width=False, height=False)
        self.bind('<Return>', self.AddTask)

        # Creating label
        self.label = Label(self,
                           text="Today's thinks to do:",
                           font=("Lucida Sans", 24),
                           bg="gray85",
                           fg="burlywood4",
                           )
        self.label.place(x=130, y=50)

        # Creating entry bar
        self.list_box = Listbox(width=30,
                                height=13,
                                font=("Lucida Sans", 18),
                                bd=0, bg="gray90",
                                fg="burlywood4",
                                highlightthickness=0,
                                activestyle="none",
                                )
        self.list_box.place(x=80, y=140)

        # Creating scrollbar
        frame = Frame(self)
        frame.place(x=513, y=140, height=364)

        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=BOTH)

        self.list_box.config(yscrollcommand=sb.set)
        sb.config(command=self.list_box.yview)

        # Creating entry bar
        self.entry_task = Entry(self,
                                width=28,
                                font=("Lucida Sans", 18),
                                bg="gray91",
                                fg="burlywood4",
                                )
        self.entry_task.place(x=92, y=530)

        # Creating buttons
        self.button_add_task = Button(self,
                                      text="Add",
                                      bg="burlywood3",
                                      padx=20,
                                      pady=10,
                                      command=self.AddTask,
                                      )
        self.button_add_task.place(x=125, y=590)

        self.button_delete_task = Button(self,
                                         text="Delete",
                                         bg="burlywood3",
                                         padx=20,
                                         pady=10,
                                         command=self.DeleteTask,
                                         )
        self.button_delete_task.place(x=195, y=590)

        self.button_load_task = Button(self,
                                       text="Load tasks",
                                       bg="burlywood3",
                                       padx=20,
                                       pady=10,
                                       command=self.LoadTask,
                                       )
        self.button_load_task.place(x=275, y=590)

        self.button_save_task = Button(self,
                                       text="Save Tasks",
                                       bg="burlywood3",
                                       padx=20,
                                       pady=10,
                                       command=self.SaveTask,
                                       )
        self.button_save_task.place(x=375, y=590)

    def AddTask(self, event=None):
        task = self.entry_task.get()
        if task != "":
            self.list_box.insert(END, " - " + task)
            self.entry_task.delete(0, END)
        else:
            messagebox.showwarning("Warning!", "You have to enter task before adding it to a list.")


    def DeleteTask(self):
        self.list_box.delete(ANCHOR)

    def SaveTask(self):
        tasks = self.list_box.get(0, self.list_box.size())
        if len(tasks) > 0:
            pickle.dump(tasks, open("tasks.dat", "wb"))
        else:
            messagebox.showwarning("Warning!", "You cannot save tasks before adding them to a list.")

    def LoadTask(self):
        tasks = pickle.load(open("tasks.dat", "rb"))
        if len(tasks) > 0:
            self.list_box.delete(0, END)
            for task in tasks:
                self.list_box.insert(END, task)
        else:
            messagebox.showwarning("Warning!", "There are any tasks saved before.")


if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
