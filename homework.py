from typing import Dict


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type: str, duration: float, distance: float,
                 speed: float, calories: float
                 ) -> None:

        self.training_type = training_type
        self.duration = round(duration, 3)
        self.distance = round(distance, 3)
        self.speed = round(speed, 3)
        self.calories = round(calories, 3)

    def get_info_string(self) -> str:
        """Формирует и возврящает строку о тренировке.
        С округлением чисел до тысячной"""

        info_string: str = f"Тип тренировки: {self.training_type}; "
        f"Длительность: {self.duration} ч.; "
        f"Дистанция: {self.distance} км; "
        f"Ср. скорость: {self.speed} км/ч; "
        f"Потрачено ккал: {self.calories}."

        return info_string


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
        spent_calories: float = (
            (coeff_calorie_1 * avg_speed - coeff_calorie_2)
            * (self.weight / self.M_IN_KM * self.duration)
        )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    LEN_STEP: float = 0.65

    def __init__(self, action: int, duration: float,
                 weight: float, height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Расчет кол-ва затраченных калорий при ходьбе по формуле:
        (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес)
        * время_тренировки_в_минутах."""

        coeff_calorie_1: float = 0.035
        coeff_calorie_2: float = 0.029
        avg_speed: float = self.get_mean_speed()
        spent_calories: float = (
            coeff_calorie_1 * self.weight + (avg_speed**2 // self.height)
            * coeff_calorie_2 * self.weight
        )
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38

    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: float, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """рассчитывает среднюю скорость при плавании по формуле:
        длина_бассейна * count_pool / M_IN_KM / время_тренировки."""

        # distance: float = self.get_distance()
        mean_speed: float = (
            self.length_pool * self.count_pool / self.LEN_STEP / self.duration
        )
        return mean_speed

    def get_spent_calories(self) -> float:
        """Затрат калорий пли плавании: (средняя_скорость + 1.1) * 2 * вес."""

        coeff_calorie_1: float = 1.1
        coeff_calorie_2: float = 2
        avg_speed: float = self.get_mean_speed()
        spent_calories: float = (
            (avg_speed + coeff_calorie_1) * coeff_calorie_2 * self.weight
        )
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    train_code: Dict[str, object] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': Warning
    }

    train_class = train_code[workout_type](*data)
    return train_class


def main(training: Training) -> None:
    """Главная функция."""

    info: InfoMessage = training.show_training_info()
    print(info.get_info_string())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
