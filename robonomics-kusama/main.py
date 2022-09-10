import logging
import time
import sys
import traceback

from classes import CoffeeMachine
from robonomicsinterface import Account, Subscriber, Datalog, SubEvent

# set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

# initialize an instance of CoffeeMachine object
coffee_machine = CoffeeMachine(gpio_outputs=[0, 21, 0, 0, 0, 0, 0])


# Define Coffee machine Robonomics account
seed: str = sys.argv[1]
coffee_acc = Account(seed=seed)
coffee_datalog = Datalog(account=coffee_acc)

logging.info("Starting main coffee machine daemon..")


def income_callback(data):

    source: str = data[0]
    amount: int = data[2]

    logging.info(f"New income from {source}: {amount} wn.")

    try:
        if amount <= 10 ** 9:
            logging.info("Insufficient income value. Coffee costs at least 1 XRT.")
        else:
            logging.info("Got enough money for making coffee. Starting...")

            operation = coffee_machine.make_a_coffee()

            if operation["success"]:
                logging.info("Operation Successful.")
                coffee_datalog.record(f"Successfully made some coffee!")
            else:
                logging.error(f"Operation Failed.")

            logging.info("Session over")
            time.sleep(100)
    except Exception:
        logging.error(f"Failed to process new income: {traceback.format_exc()}")


Subscriber(
    account=coffee_acc,
    subscribed_event=SubEvent.Transfer,
    subscription_handler=income_callback,
    addr=coffee_acc.get_address(),
)
