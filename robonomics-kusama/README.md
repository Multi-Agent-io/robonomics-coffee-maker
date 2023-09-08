This guide demonstrates how to operate [an automated coffee machine on the blockchain](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master) within the Robonomics parachain, a part of the Polkadot ecosystem.

## Software installation

- Prepare the Raspberry Pi for Substrate libraries by installing [Rust](https://www.rust-lang.org/tools/install):
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup default nightly
```

- Install [GPIO Zero library](https://gpiozero.readthedocs.io/en/stable/installing.html) and reboot the Raspberry Pi:
```bash
sudo apt update
sudo apt install python3-gpiozero
sudo reboot
```

- Clone the repository:
```bash
git clone https://github.com/Multi-Agent-io/robonomics-coffee-maker
```
- Install project requirements:
```bash
pip3 install -r requirements.txt
```

## Account management
To use the coffee machine, you'll need a Polkadot account. Create a new account using your preferred extension. If you're unsure how to do this, please refer to the official [documentation](https://support.polkadot.network/support/solutions/articles/65000098878-how-to-create-a-dot-account). **Ensure that you keep your mnemonic phrase secret and secure.**

## Run Robonomics coffee
Run this within the repository folder:
```bash
python3 main.py "mnemonic phrase of a Polkadot account for the coffee machine"
```
You can send XRT tokens from another account. Once there is incoming XRT, the Raspberry Pi triggers GPIO pin 18, and the coffee machine starts brewing coffee!

[Discover how to explore further development](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master#exploring-further-development)
