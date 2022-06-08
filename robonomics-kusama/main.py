import logging
import time
import sys

from classes import CoffeeMachine
from robonomicsinterface import RobonomicsInterface as RI
from statemine_monitor import ACTIncomeTracker
from substrateinterface import Keypair

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# initialize an instance of CoffeeMachine object
coffee_machine = CoffeeMachine(
    gpio_outputs=[0, 21, 0, 0, 0, 0, 0]
)


# Define Statemine sss58_address from seed
seed: str = sys.argv[1]
keypair = Keypair.create_from_mnemonic(seed, ss58_format=2)

# Start income tracker
income_tracker = ACTIncomeTracker(keypair.ss58_address)

# Start coffee machine daemon
logging.info("Started main coffee machine daemon")
while True:
    # wait for money income event
    income_tracker.act_income_event.wait()
    income_tracker.act_income_event.clear()
    operation = coffee_machine.make_a_coffee()

    if operation["success"]:
        logging.info("Operation Successful.")
        try:
            # Initiate RobonomicsInterface instance
            ri_interface = RI(seed=seed)
            ri_interface.record_datalog(f"Successfully made some coffee!")
        except Exception as e:
            logging.error(f"Failed to record Datalog: {e}")
    else:
        logging.error(f"Operation Failed.")
        try:
            # Initiate RobonomicsInterface instance
            ri_interface = RI(seed=seed)
            ri_interface.record_datalog(f"Failed to make coffee: {operation['message']}")
        except Exception as e:
            logging.error(f"Failed to record Datalog: {e}")
    logging.info("Session over")
    time.sleep(100)