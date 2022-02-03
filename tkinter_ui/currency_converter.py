import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class CurrencyConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Currency Converter")

        self.frames = {}

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        for FrameClass in (EurToHuf,HufToEur):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        
        self.show_frame(EurToHuf)
        
    def show_frame(self, container):
        frame = self.frames[container]
        # self.bind("<Enter>", frame.calculate)
        # self.bind("<KP_Enter>", frame.calculate)
        frame.tkraise()


class EurToHuf(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.eur = tk.StringVar()
        self.huf = tk.StringVar()

        eur_label = ttk.Label(self, text="Eur: ")
        eur_entry = ttk.Entry(self, width=10, textvariable=self.eur, font=("Segoe UI", 15))

        huf_label = ttk.Label(self, text="Huf: ")
        huf_value = ttk.Label(self, textvariable=self.huf)

        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)

        switch_page_button = ttk.Button(self, text= " Switch to HUF conversation",
        command= lambda: controller.show_frame(HufToEur))

        eur_label.grid(column=0, row=0, sticky="W")
        eur_entry.grid(column=1, row=0, sticky="EW")
        huf_label.grid(column=0, row=1, sticky="W")
        huf_value.grid(column=1, row=1, sticky="EW")
        

        eur_entry.focus()

        calc_button.grid(row=2, column=0, sticky="W")
        switch_page_button.grid(row=2, column=1, sticky="EW")

    def calculate(self):
        try:
            eur = float(self.eur.get())
            huf = eur * 356.34
            self.huf.set(f"{huf: 3f}")
        except ValueError:
            pass

class HufToEur(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.eur = tk.StringVar()
        self.huf = tk.StringVar()

        huf_label = ttk.Label(self, text="Huf: ")
        huf_entry = ttk.Entry(self, width=10, textvariable=self.huf, font=("Segoe UI", 15))

        eur_label = ttk.Label(self, text="Eur: ")
        eur_value = ttk.Label(self, textvariable=self.eur)

        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(self, text= " Switch to EUR conversation",
        command= lambda: controller.show_frame(EurToHuf))


        huf_label.grid(column=0, row=0, sticky="W")
        huf_entry.grid(column=1, row=0, sticky="EW")
        eur_label.grid(column=0, row=1, sticky="W")
        eur_value.grid(column=1, row=1, sticky="W")

        calc_button.grid(row=2, column=0, sticky="W")
        switch_page_button.grid(row=2, column=1, sticky="EW")


    def calculate(self):
        try:
            huf = float(self.huf.get())
            eur = huf/356.34
            self.eur.set(f"{eur: 3f}")
        except ValueError:
            pass


if __name__ == '__main__':
    root = CurrencyConverter()
    font.nametofont("TkDefaultFont").configure(size=15)

    root.columnconfigure(0, weight=1)

    root.mainloop()