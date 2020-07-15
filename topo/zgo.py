import math
from topo.point import Point
from topo.func import *


class ZGO:
    CIRCLE_ANGLE = 6000

    def __init__(self, A_cords: str, B_cords: str, Kz: int=0):
        """
        :param A_cords: współrzędne SO
        :param B_cords: współrzędne celu
        :param Kz: kierunek zasadniczy, domyślnie 00-00

        :def set_circle_angle(value: int)
        Ustawia wartość kąta pełnego na value
        """
        self.Kz = Kz
        self.known_values = {}

        if are_valid_cords(A_cords) and are_valid_cords(B_cords):
            self.A = Point(A_cords)
            self.B = Point(B_cords)
        else:
            raise ValueError("Współrzędne są nieprawidłowe!")

    def get_results(self):
        """
        if Kz != 0:
            :return: distance, kp_Kz
        else:
            :return: distance, kp_Kz = direction = T
        """
        distance = self.cal_distance()
        direction = self.cal_direction()
        kp_Kz = (int(round(direction - self.Kz, 0)))
        self.known_values["kp_Kz"] = kp_Kz
        return distance, kp_Kz

    def get_details(self):
        if "distance" not in self.known_values:
            self.get_results()

        N_C = self.B.x
        N_SO = self.A.x
        delta_N = self.known_values["delta_x"]
        E_C = self.B.y
        E_SO = self.A.y
        delta_E = self.known_values["delta_y"]
        k = self.known_values["k"]
        t = self.known_values["t"]
        t_tys = self.known_values["t_mils"]
        T_SO_C = self.known_values["direction"]
        T_Kz = self.Kz
        kp_Kz = self.known_values["kp_Kz"]
        t_rad = math.radians(t)
        D_1 = 1 / math.sin(t_rad)
        D_TC_1 = int(round(D_1 * delta_E, 0))
        D_2 = 1 / math.cos(t_rad)
        D_TC_2 = int(round(D_2 * delta_N, 0))
        D_TC_3 = self.known_values["distance"]

        k = round(k, 5)
        t = round(t, 5)
        D_1 = round(D_1, 5)
        D_2 = round(D_2, 5)
        return N_C, N_SO, delta_N, E_C, E_SO, delta_E, k, t,\
               t_tys, T_SO_C, T_Kz, kp_Kz, D_1, D_TC_1, D_2,\
               D_TC_2, D_TC_3

    def cal_distance(self):
        delta_x = self.B.x - self.A.x
        delta_y = self.B.y - self.A.y
        distance = int(round(math.sqrt(delta_y**2 + delta_x**2), 0))
        self.known_values.update({
            "delta_x": delta_x,
            "delta_y": delta_y,
            "distance": distance
        })
        return distance

    def cal_direction(self):
        delta_y = self.known_values["delta_y"]
        delta_x = self.known_values["delta_x"]
        k = delta_y / delta_x
        t = math.degrees(math.atan(k))
        t_mils = int(round(self.CIRCLE_ANGLE * t / 360, 0))
        direction = t_mils
        quater = get_quarter(delta_y, delta_x)
        quater_val = self.CIRCLE_ANGLE // 4
        min_val = (quater - 1) * quater_val
        max_val = min_val + quater_val
        while direction >= max_val:
            direction -= quater_val

        while direction <= min_val:
            direction += quater_val

        self.known_values.update({
            "k": k,
            "t": t,
            "t_mils": t_mils,
            "direction": direction
        })
        return direction

    @classmethod
    def set_circle_angle(cls, value: int):
        cls.CIRCLE_ANGLE = value


if __name__ == "__main__":
    ##########################
    DETAILED = False
    ##########################
    A_cords = "9474285375"
    B_cords = "6437593648"
    Kz = 2367
    ##########################
    zgo = ZGO(A_cords, B_cords, Kz)
    if DETAILED:
        values = zgo.get_details()
        result = ""
        for val in values:
            result += str(val) + "\n"
    else:
        distance, kp_Kz = zgo.get_results()
        result = f"""D_TC = {distance}
kp_Kz = {kp_Kz}"""

    print(result)
