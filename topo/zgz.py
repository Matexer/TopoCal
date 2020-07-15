import math
from topo.func import are_valid_cords
from topo.point import Point


class ZGZ:
    CIRCLE_ANGLE = 6000

    def __init__(self, A_cords: str, direction: int, distance: int):
        """
        :param A_cords:  str
        :param direction:  int
        :param distance:  int

        :def set_circle_angle(value: int)
        Ustawia wartość kąta pełnego na value
        """
        self.known_values = {}
        self.direction = direction
        self.distance = distance

        if are_valid_cords(A_cords):
            self.A = Point(A_cords)
            self.B = Point(A_cords)
        else:
            raise ValueError("Nieprawidłowa wartość współrzędnych!")

    def get_results(self):
        direction_deg = self.direction * 360 / self.CIRCLE_ANGLE
        direction_rad = math.radians(direction_deg)
        sin_T = math.sin(direction_rad)
        delta_y = self.distance * sin_T
        cos_T = math.cos(direction_rad)
        delta_x = self.distance * cos_T
        delta_y = int(round(delta_y, 0))
        delta_x = int(round(delta_x, 0))
        self.B.move(delta_y, delta_x)
        self.known_values.update({
            "direction_deg": direction_deg,
            "direction_rad": direction_rad,
            "sin_T": sin_T,
            "cos_T": cos_T,
            "delta_y": delta_y,
            "delta_x": delta_x,
        })
        return self.B.get_cords()

    def get_details(self):
        if "direction_deg" not in self.known_values:
            self.get_results()

        E_PO = self.A.y
        N_PO = self.A.x
        T_PO_C = self.direction
        T_PO_C_deg = self.known_values["direction_deg"]
        d_PO_C = self.distance
        sin_T_PO_C = self.known_values["sin_T"]
        delta_E = self.known_values["delta_y"]
        cos_T_PO_C = self.known_values["cos_T"]
        delta_N = self.known_values["delta_x"]
        E_C = self.B.y
        N_C = self.B.x

        T_PO_C_deg = int(round(T_PO_C_deg, 0))
        sin_T_PO_C = round(sin_T_PO_C, 5)
        cos_T_PO_C = round(cos_T_PO_C, 5)

        return E_PO, N_PO, T_PO_C, T_PO_C_deg, d_PO_C, sin_T_PO_C,\
               delta_E, cos_T_PO_C, delta_N, E_C, N_C

    @classmethod
    def set_circle_angle(cls, value: int):
        cls.CIRCLE_ANGLE = value


if __name__ == "__main__":
    ##########################
    DETAILED = False
    ##########################
    A_cords = "9474285375"
    T = 2344
    d = 5447
    ##########################
    zgz = ZGZ(A_cords, T, d)
    if DETAILED:
        values = zgz.get_details()
        result = ""
        for val in values:
            result += str(val) + "\n"
    else:
        cords = zgz.get_results()
        result = cords

    print(result)
