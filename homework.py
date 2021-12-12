from typing import ClassVar, Dict, List, Type
from dataclasses import asdict, dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    INFO_MESSAGE: ClassVar[str] = (
        "Тип тренировки: {training_type}; "
        "Длительность: {duration:.3f} ч.; "
        "Дистанция: {distance:.3f} км; "
        "Ср. скорость: {speed:.3f} км/ч; "
        "Потрачено ккал: {calories:.3f}."
    )

    def get_message(self) -> str:
        """Формирует и возврящает строку о тренировке."""
        return self.INFO_MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65

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
        raise NotImplementedError(
            "Определите get_spent_calories в %s." % (self.__class__.__name__))

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = self.__class__.__name__
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        info: InfoMessage = InfoMessage(training_type, self.duration,
                                        distance, speed, calories)
        return info


class Running(Training):
    """Тренировка: бег."""

    COEF_CALL_1: float = 18
    COEF_CALL_2: float = 20
    MIN_IN_HOUR: int = 60

    def get_spent_calories(self) -> float:
        """Получить кол-во затраченных калорий при беге, по формуле:
        (18 * средняя_скорость - 20)
         * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах.
        """
        duration_min = self.duration * self.MIN_IN_HOUR
        spent_calories: float = (
            (self.COEF_CALL_1 * self.get_mean_speed() - self.COEF_CALL_2)
            * self.weight / self.M_IN_KM * duration_min
        )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    COEF_CALL_1: float = 0.035
    COEF_CALL_2: float = 0.029
    MIN_IN_HOUR: int = 60

    def __init__(self, action: int, duration: float,
                 weight: float, height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Расчет кол-ва затраченных калорий при ходьбе по формуле:
        (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес)
        * время_тренировки_в_минутах.
        """
        duration_min = self.duration * self.MIN_IN_HOUR
        spent_calories: float = (
            (self.COEF_CALL_1 * self.weight
                + (self.get_mean_speed()**2 // self.height)
                * self.COEF_CALL_2 * self.weight) * duration_min
        )
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    COEF_CALL_1: float = 1.1
    COEF_CALL_2: float = 2

    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: float, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Pассчитывает среднюю скорость при плавании по формуле:
        длина_бассейна * count_pool / M_IN_KM / время_тренировки.
        """
        mean_speed: float = (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )
        return mean_speed

    def get_spent_calories(self) -> float:
        """Затрат калорий пли плавании: (средняя_скорость + 1.1) * 2 * вес."""
        spent_calories: float = (
            (self.get_mean_speed() + self.COEF_CALL_1)
            * self.COEF_CALL_2 * self.weight
        )
        return spent_calories


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков.
    Если нет типа тренировки, переданного в workout_type, возбудить исключение,
    Если есть вернуть экземпляр нужного класса.
    """
    training_codes_and_classes_mapping: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type in training_codes_and_classes_mapping:
        return training_codes_and_classes_mapping[workout_type](*data)

    raise KeyError(
        "Вид тренировки с ключем '%s' не зарегистрирован в программе."
        % (workout_type)
    )


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
