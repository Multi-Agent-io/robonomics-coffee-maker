## Installation
- Install gpiozero library ([source](https://gpiozero.readthedocs.io/en/stable/installing.html)) and reboot:
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo reboot
```
- Clone the repository
```bash
git clone https://github.com/Multi-Agent-io/robonomics-coffee-maker
cd robonomics-coffee-maker
```

- Install Node.js requirements
```bash
npm install @eversdk/core
npm install python-shell
mv eversdk.node ~/.tonlabs/binaries/1
git clone https://github.com/tonlabs/ever-sdk-js
cd ever-sdk-js/packages/lib-node
npm install -g
```

The reason why we can't just npm install @eversdk/lib-node is because this library is not compiled for the ARM architecture.

## Account management
If you want to change coffee machine address you can do it in main.js. By default, cost of coffee is 0.5 EVER, but you can change it in main.js too.

## Run Robonomics coffee
Run poller by 
```bash
node main.js
```
## Things to point out
Now, if you will send 0.5 EVER to coffee machine address, poller will catch transaction and execute `make_coffee.py`.
You can create a qr code to make it easy to use. Example: ![Screenshot](qr.jpg)  
Just encode ton://transfer/YourCoffeeMachineAddress?amount=AmountIngrams