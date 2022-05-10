import logging
import threading
import typing as tp
from substrateinterface import SubstrateInterface

# set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)


class ACTIncomeTracker:
    """
    Income tracker of ACT in Statemine Kusama parachain
    """

    def __init__(self, address: str):
        """
        Initiating instance of a class, create substrate connection, start a subscriber for incomes on a specified
        address

        @param address: Coffee Machine ss58_address in Statemine Kusama parachain
        """

        self._address: str = address
        self._assetid: int = 3077  # ACT asset ID in Statemine Kusama parachain
        self._current_act_balance: int

        logging.info("Creating an instance of an IncomeTracker class")
        logging.info("Initiating Statemine connection")

        self._interface: SubstrateInterface = SubstrateInterface(
            url="wss://statemine-rpc.polkadot.io"
        )

        logging.info(f"Initiating asset subscriber for incomes obtaining")
        self.act_income_event = threading.Event()

        self._subscriber = threading.Thread(target=self._obtain_incomes)
        self._subscriber.start()

        logging.info("Asset subscriber started. Waiting for money incomes")

    def _handle_incomes(self, obj: tp.Any, update_nr: int, subscription_id: int):
        """
        Check ACT balance update and set Python Event on money income

        @param obj: updated chainstate output
        @param update_nr: update counter
        @param subscription_id: subscription id
        """
        _new_act_balance: int = obj.value["balance"]

        if update_nr == 0:  # initial subscriber trigger
            self._current_act_balance = _new_act_balance

        if update_nr > 0:
            if _new_act_balance > self._current_act_balance:
                logging.info(f"Money income: {_new_act_balance - self._current_act_balance} ACT token(s)")
                self._current_act_balance = _new_act_balance
                self.act_income_event.set()

    def _obtain_incomes(self):
        """
        Subscribe to new chainstate events as soon as they are available. The callable `_handle_incomes` will be
        executed then and execution will block until `subscription_handler` will return a result other than `None`
        """

        self._interface.query("Assets", "Account", [self._assetid, self._address],
                              subscription_handler=self._handle_incomes)


if __name__ == '__main__':

    income_tracker = ACTIncomeTracker("")
    logging.info("Waiting for money income")
    while True:
        income_tracker.act_income_event.wait()
        print("Event set")
        income_tracker.act_income_event.clear()
