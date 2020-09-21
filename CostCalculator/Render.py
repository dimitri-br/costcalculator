import tkinter as tk
import tkinter.font as font




class Renderer:
    def __init__(self, title="Tkinter App"):
        self.tk = tk.Tk()
        self.tk.title(title)
        self.tk.configure(bg='black')
        self.add_widgets()

    def add_widgets(self):
        l = tk.Label(self.tk, text="Sum of wall height (All wall heights added)[m]:", font=("Times", 18, "bold"), fg="white", bg="black").pack()

        self.height = tk.Entry(self.tk, font=("Times", 14))
        self.height.pack()

        l = tk.Label(self.tk, text="Sum of wall width (All wall widths added)[m]:", font=("Times", 18, "bold"), fg="white", bg="black").pack()


        self.width = tk.Entry(self.tk, font=("Times", 14))
        self.width.pack()

        self.check = tk.IntVar()
        l = tk.Label(self.tk, text="Is the floor carpet:", font=("Times", 18, "bold"), fg="white", bg="black").pack()

        tk.Checkbutton(self.tk, variable=self.check, font=("Times", 18, "bold"), fg="black", bg="black").pack()

        l = tk.Label(self.tk, text="Floor Area [m²]:", font=("Times", 18, "bold"), fg="white", bg="black").pack()

        self.floor = tk.Entry(self.tk, font=("Times", 14))
        self.floor.pack()

        tk.Button(self.tk, text="Calculate", command=self.calculate_costs).pack()

        l = tk.Label(self.tk, text="Cost:", font=("Times", 18, "bold"), fg="white", bg="black").pack()

        self.cost = tk.Label(self.tk, text="", font=("Times", 18, "bold"), fg="white", bg="black")
        self.cost.pack()

    def calculate_costs(self):
        from . import Calculator
        try:
            cc = Calculator.CostCalculator()

            cc.set_wall_area(int(self.width.get()), int(self.height.get()))
            cc.set_floor_area(int(self.floor.get()))
            if self.check == 0:
                isChecked = False
            else:
                isChecked = True
            costs = cc.calculate_costs(isChecked)
            print(f"Floor cost: £{costs[0]} for {cc.floor_area} m2\nWall cost: £{costs[1]} for {cc.wall_area} m2")
            self.cost["text"] = f"Redecorating costs: £{str(round(costs[0]+costs[1], 2))}"

        except BaseException as e:
            print(f"Error calculating cost - {e}")

    def loop(self):
        self.tk.mainloop()
