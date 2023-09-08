This guide demonstrates how to operate [an automated coffee machine on the blockchain](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master) within the [Everscale network](https://everscale.network).

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
npm install @eversdk/core
npm install python-shell
mv eversdk.node ~/.tonlabs/binaries/1
git clone https://github.com/tonlabs/ever-sdk-js
cd ever-sdk-js/packages/lib-node
npm install -g
```

The reason we can't simply use 'npm install @eversdk/lib-node' is because this library is not compiled for the ARM architecture.

## Account management
To use the coffee machine, you'll need an Everscale account.

You can modify the coffee machine address, the cost of one cup of coffee, or the endpoint in the [main.js](https://github.com/Multi-Agent-io/robonomics-coffee-maker/blob/master/everscale/main.js) file. You can also customize the GPIO codes for operating the coffee machine in the [make_coffee.py](https://github.com/Multi-Agent-io/robonomics-coffee-maker/blob/master/everscale/make_coffe.py) file.

## Brew coffee using the blockchain coffee machine
Run poller by 
```bash
node main.js
```
Now, when you send 0.5 EVER to the coffee machine address, poller will catch transaction and execute `make_coffee.py`, and the coffee machine will start brewing coffee!

## QR codes
For convenient transfers, you can utilize a QR code. To do this, encode `ton://transfer/YourCoffeeMachineAddress?amount=AmountIngrams` into a QR code.

## [Discover how to explore further development](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master#exploring-further-development)
