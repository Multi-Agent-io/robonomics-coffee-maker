This guide demonstrates how to operate [an automated coffee machine on the blockchain](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master) within the [Robonomics](https://robonomics.network) parachain, a part of the Polkadot ecosystem.

## Software installation


- Install [GPIO Zero library](https://gpiozero.readthedocs.io/en/stable/installing.html) and reboot the Raspberry Pi:
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo reboot
```

- Clone the repository and navigate to the repository's folder:
```bash
git clone https://github.com/Multi-Agent-io/robonomics-coffee-maker
cd robonomics-coffee-maker
```

- Install project requirements:
```bash
pip3 install -r requirements.txt
```

## Account management
To use the coffee machine, you'll need a Polkadot account. Create a new account using your preferred extension. If you're unsure how to do this, please refer to the official [documentation](https://support.polkadot.network/support/solutions/articles/65000098878-how-to-create-a-dot-account). **Ensure that you keep your mnemonic phrase secret and secure.**

You can modify the coffee machine address, the cost of one cup of coffee, or the GPIO codes for operating the coffee machine in the [main.py](https://github.com/Multi-Agent-io/robonomics-coffee-maker/blob/master/robonomics-kusama/main.py) file.

## Brew coffee using the blockchain coffee machine
Run this within the repository folder:
```bash
python3 main.py "mnemonic phrase of a Polkadot account for the coffee machine"
```
Now, when you send 1 XRT to the coffee machine address, the subscriber will detect the transaction, activate the espresso button (in our case, the Raspberry Pi triggers GPIO pin 18), and the coffee machine will start brewing coffee!

## QR codes
![QR codes for paying to the blockchain coffee machine](../readme-assets/qrcodes-blockchain-smart-coffee-machine.jpg?raw=true)
For convenient transfers, you can utilize a QR code. To do this, encode the Polkadot account address that you've created for the coffee machine into a QR code.

## [Discover how to explore further development](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master#exploring-further-development)
