from tonclient.types import ClientConfig, ParamsOfQuery
from tonclient.client import TonClient, DEVNET_BASE_URLS
from time import sleep
from classes import CoffeeMachine
from loguru import logger

client_config = ClientConfig()
client_config.network.endpoints = DEVNET_BASE_URLS    #you can change network here
client = TonClient(config=client_config)


coffee_machine = CoffeeMachine(
    gpio_outputs=[0, 21, 0, 0, 0, 0, 0]
)


#change lighthouse address here
def get_coffe_machine_transactions():
  return client.net.query(
        params=ParamsOfQuery(
            """
    query {
      blockchain{
      account(address:"0:34f36279f650b703e306e6f5bb200d4f47e7852f34da01667c08e8769e601801"){
        transactions{
          edges{
            node{
              id
              hash
              in_msg
              out_msgs
              balance_delta(format:DEC)
              total_fees(format:DEC)
            }
          }
          pageInfo{
            endCursor
            hasNextPage
          }
        }
      }
      }
    }
    """
        )
    ).result['data']['blockchain']['account']['transactions']['edges']


# def make_coffee():
#     print('Making coffee...')


def main():

  print('Start polling...')
  
  transactions_count = len(get_coffe_machine_transactions())

  print('Transactions count: ', transactions_count )
  while True:
    res = get_coffe_machine_transactions()
    if len(res) == transactions_count:
      sleep(1)
      continue
    
    print('Transaction catched!')

    transactions_count = len(res)
    
    last_transaction = res[-1]

    if float(last_transaction['node']['balance_delta']) + float(last_transaction['node']['total_fees']) >= 0.5 * 10 ** 9:    #0.5 EVER
      coffee_machine.make_a_coffee()
    else:
      logger.warning(f"{float(last_transaction['node']['balance_delta'])} < {0.5 * 10 ** 9}")
    


if __name__ == '__main__':
  main()

