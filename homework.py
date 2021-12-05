class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        distance: float = self.get_distance()
        mean_speed: float = distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""

    LEN_STEP: float = 0.65

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить кол-во затраченных калорий при беге, по формуле:
        (18 * средняя_скорость - 20)
         * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах."""

        coeff_calorie_1: float = 18
        coeff_calorie_2: float = 20
        avg_speed: float = self.get_mean_speed()
        spent_calories: float = (coeff_calorie_1 * avg_speed - coeff_calorie_2)
        spent_calories *= self.weight / self.M_IN_KM * self.duration
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    LEN_STEP: float = 0.65

    def __init__(self, action: int, duration: float,
                 weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Расчет кол-ва затраченных калорий при ходьбе по формуле:
        (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес)
        * время_тренировки_в_минутах."""

        coeff_calorie_1: float = 0.035
        coeff_calorie_2: float = 0.029
        avg_speed: float = self.get_mean_speed()
        spent_calories: float = coeff_calorie_1 * self.weight
        spent_calories += (avg_speed**2 // self.height)
        spent_calories *= coeff_calorie_2 * self.weight
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
