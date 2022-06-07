# Robonomics Coffee

## About
"Robonomics coffee" - is a smart coffee machine integrated in  [Robonomics Network](https://robonomics.network/).
This project aims to show Robonomics potential in the IoT sphere by a real-world example. More info and tutorial may be
found in [Robonomcis Wiki](https://wiki.robonomics.network/docs/en/robonomics-coffee/)

## Software installation
- Install gpiozero library ([source](https://gpiozero.readthedocs.io/en/stable/installing.html)) and reboot:
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo pip3 install gpiozero
sudo reboot
```
- Clone the repository
```bash
git clone https://github.com/Multi-Agent-io/robonomics-coffee-maker
```
- Install python requirements
```bash
pip3 install -r requirements.txt
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

## Account management
If you want to change coffe maching address you can do it in main.js. By default cost of coffe is 0.5 EVER, but you can change it in main.js too.

## Run Robonomics coffee
Run poller by 
```bash
node main.js
```
## Things to point out
Now, if you will send 0.5 EVER to coffe machine address, poller will catch transaction and execute make_coffe.py.
You can create a qr code to make it easy to use. Example: ![Screenshot](qr.jpg)  
Just encode ton://transfer/YourCoffeMachineAddress?amount=AmountIngrams