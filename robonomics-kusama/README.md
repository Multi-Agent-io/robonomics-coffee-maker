## Installation
- Prepare the RPI for Substrate libs ([source](https://www.rust-lang.org/tools/install)):
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup default nightly
```
- Install gpiozero library ([source](https://gpiozero.readthedocs.io/en/stable/installing.html)) and reboot:
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo reboot
```
- Clone the repository
```bash
git clone https://github.com/Multi-Agent-io/robonomics-coffee-maker
```
- Install project requirements
```bash
pip3 install -r requirements.txt
```

## Account management
On your PC install [Polkadot Extension](https://polkadot.js.org/extension/) and register a coffee-machine account there. **Save 
mnemonic seed phrase as it is going to be used later.**

Logging actions in Robonomics is optional, you will need XRT on 
[parachain.robonomics.network](https://parachain.robonomics.network/) for coffee-machine account (it is the same across
networks) for this. If not, there will simply be an error message *"Balance too low."*

## Run Robonomics coffee
Run this in repo folder:
```bash
python3 main.py <previously saved seed>
```
You can send tokens from another account created the same way via `assets:transfer` *extrinsic* on 
[Statemine](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fkusama-statemine-rpc.paritytech.net#/explorer).

As soon as there is an income (positive change in `assets:account` *storage function* for address 
derived from seed and for token id `3077`) the RPI triggers GPIO pin 18 and coffee machine starts making coffee!

## Things to point out
- This is a POC of a blockchain-driven IoT device, it has things to improve, wires to hide and functionality to implement
- Token ID, the one, coffee-machine is waiting to receive is edited
[here](https://github.com/Multi-Agent-io/robonomics-coffee-maker/blob/master/statemine_monitor.py#L27), so you can use your own token
- Right now the only thing that matters for income tracker is the positive difference between current and previous
asset balance. This may be filtered [code](https://github.com/Multi-Agent-io/robonomics-coffee-maker/blob/master/statemine_monitor.py#L59).
- Powered by [Robonomics](https://robonomics.network/), made by [Multi-Agent.io](https://multi-agent.io/).