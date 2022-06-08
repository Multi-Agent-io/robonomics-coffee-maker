from classes import CoffeeMachine
import sys

coffee_machine = CoffeeMachine(
    gpio_outputs=[0, 21, 0, 0, 0, 0, 0]
)

coffee_machine.make_a_coffee()

print("Started making coffe...")
sys.stdout.flush()