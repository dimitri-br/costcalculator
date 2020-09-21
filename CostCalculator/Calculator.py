class CostCalculator:
    def __init__(self):
        self.wall_area = 0  # in m^2
        self.floor_area = 0  # in m^2

        self.__base_paint_cost = 10  # cost per liter
        self.__base_floor_cost = 5  # cost per m2
        self.__base_carpet_cost = 15  # cost per m2

    def set_floor_area(self, area):
        self.floor_area = area

    def set_wall_area(self, height=10, width=5):
        self.wall_area = height * width

    def calculate_costs(self, is_carpet):
        if is_carpet:
            floor_cost = self.floor_area * self.__base_carpet_cost
        else:
            floor_cost = self.floor_area * self.__base_floor_cost

        wall_cost = ((self.wall_area * 4) / 12) * self.__base_paint_cost

        return floor_cost, wall_cost
