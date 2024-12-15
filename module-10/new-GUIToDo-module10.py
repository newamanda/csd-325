#Amanda New
#CSD325-A311
#Module 10
#GUI ToDo

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else: 
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        #***Create menu to exit
        self.menu = tk.Menu(self, bg="lightgrey", fg="black")

        self.exit_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.exit_menu.add_command(label="Exit", command=self.exit_app)

        self.menu.add_cascade(label="File", menu=self.exit_menu)

        self.config(menu=self.menu)
        #***

        self.title("New-ToDo")
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        
        #**Changed color from light grey to tomato***
        #**Added instructions on how to delete a task***
        todo1 = tk.Label(self.tasks_frame, text="---Add Items Here---\nTo Delete Task: Right Click", bg="tomato", fg="black", pady=10)
        
        #***Changed button-1(left click) to button-3(right click***)
        todo1.bind("<Button-3>, self.remove_task")

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        #**Changed color from light grey to tomato, and grey to lightseagreen***
        self.colour_schemes = [{"bg": "tomato", "fg" : "black"}, {"bg": "lightseagreen", "fg": "white"}]
    
    #***function to close app when user selects "Exit" from "File" menu
    def exit_app(self):
        self.quit()
    #***
    
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            self.set_task_colour(len(self.tasks), new_task)

            #***Changed button-1(left click) to button-3(right click***)
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()