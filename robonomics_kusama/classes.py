import typing as tp
import rpi_funcs as rpi
import logging

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)


class CoffeeMachine:
    """handles operating the coffee maker using RPI's GPIO"""

    def __init__(self, gpio_outputs: tp.List[int]) -> None:
        # map different control panel buttons to corresponding GPIO channels
        self.button_map: tp.Dict[str, int] = {
            "power": 0,
            "one_small_cup": 0,
            "two_small_cups": 0,
            "steam": 0,
            "rinse": 0,
            "one_big_cup": 0,
            "two_big_cups": 0
        }

        # apply provided values to their buttons
        for value in zip(gpio_outputs, self.button_map.keys()):
            if value[0]:
                self.button_map[value[1]] = value[0]

        logging.info("initialized CoffeeMachine instance")

    def make_a_coffee(self) -> tp.Dict[str, tp.Any]:
        """
        pours a cup of coffee

        :returns: {"success": bool, "message": str}"""

        rpi.trigger_transistor(self.button_map["one_small_cup"])

        operation = {
            "success": True,
            "message": "operation success"
        }

        logging.info("Made a coffee")
        return operation
