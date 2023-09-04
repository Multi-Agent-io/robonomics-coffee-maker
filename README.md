# Blockchain-powered smart coffee machine

## About
The 'Robonomics Coffee' is a smart coffee machine integrated into the Robonomics Network. This project serves as a practical demonstration of Robonomics' capabilities within the IoT realm. It seeks to address questions such as whether we can foster democracy through smart contracts, how to resolve the 'tragedy of the commons' dilemma in the office using innovative decentralized technologies, and how to employ Web3 and blockchain for automating smart spaces. Find out more about this concept [here](https://robonomics.network/cases/blockchain-coffee-machine/)

Here you can find a detailed tutorial and technical specifications for DIY your own blockchain automated coffee machine. Keep in mind that you can use any coffee machine you prefer and almost any token of your choice to bring this project to life in your own space.

## Setting up the hardware

Here, you will see how we accomplished this. This example can also be applied to the coffee machine of your choice.

### You will need
- **The coffee machine.** When selecting a coffee machine, consider how you'll interact with it.  We decided to simulate button presses using GPIO, so we looked for a model where we could solder wires to the control panel. We settled on the [De’Longhi Magnifica ECAM 22.110](https://www.delonghi.com/en/ecam22-110-sb-magnifica-s-automatic-coffee-maker/p/ECAM22.110.SB) because it's budget-friendly and has an easily removable front panel. It's a no-frills machine with basic buttons, perfect for making espresso.
- **A single-board computer.** Specifically the Raspberry Pi 4 (2GB), and installed the Ubuntu server using the [RPi Imager application](https://www.raspberrypi.com/software/).
- **A 5V adapter and a USB-A to USB Type-C cable** The adapter can be similar to [this](https://www.amazon.com/Charger-FOBSUNLAND-Universal-Adapter-S6-Note/dp/B073Q1N8FL), and the cable should look like [this](https://www.amazon.com/Charger-Braided-Charging-Compatible-Samsung/dp/B0794M53HQ).
- **F-M (female-male), M-M (male-male), and F-F (female-female) jumper wires, as well as a breadboard.** This should look like [this](https://www.amazon.com/Standard-Jumper-Solderless-Prototype-Breadboard/dp/B07H7V1X7Y)
- **A transistor and a resistor (optionally).**

Additionally, make sure to have a set of screwdrivers, a soldering iron with solder and flux, and a multimeter on hand.

### Disassemble the coffee machine

Our objective is to detach the front panel (which won't be used anymore) and separate the control PCB. You can find [a helpful tutorial](https://youtu.be/7Y5NCePD0PM?feature=shared) on YouTube as a reference.

### Solder two wires to the required button

Solder them to the isolated contacts, which, in our case, are the two bottom contacts. You can use any wires, but remember that one of them should be an M-wire for connecting it to the breadboard later.

### Reassemble the coffee machine
Now, reassemble the coffee machine by reinstalling the PCB control board. Keep the front panel removed.

### Connecting the coffee machine to Raspberry Pi

#### Circuit

The complete circuit is shown below. It's a straightforward transistor switch configuration. We employed R1=1kΩ, an NPN transistor Q1 (with specifications hfe=40, Uce>5V, Ic>0.015A; we have a sample here, but almost any general-purpose transistor will suffice since it's acting as a switch), and a small 3.3V diode D in the base circuit, which we found in our lab's storage. Alternatively, you can use a MOSFET transistor.

#### Wires

Connect the wires labeled as RPI GND and RPI GPIO Pin to pins GND and 21, respectively, according to the RPI GPIO scheme shown below. The wires marked as Button+ and Button- should be connected to the left button contact and right button contact, respectively.

## Software installation

Let's transform this hardware into a blockchain-powered automated coffee machine!

### Choose network

We worked on this project in two different networks, [Robonomics Kusama Parachain](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fkusama.rpc.robonomics.network%2F#/explorer)  and [Everscale](https://net.ever.live/). As a result, we have two subprojects with slight variations in income tracking. You can find them in separate folders within this repository.

Also, for each subproject there is a generated `systemd service` file to be put in `/etc/systemd/system`.
**Edit script paths in them first** and then move these files.

```bash
sudo mv robonomics_coffee_maker_everscale.service /etc/systemd/system
sudo mv robonomics_coffee_maker_robonomics_kusama.service /etc/systemd/system
```

### Follow the instructions for your chosen network

- [Installation in Robonomics Kusama Parachain](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master/robonomics-kusama)
- [Installation in Everscale](https://github.com/Multi-Agent-io/robonomics-coffee-maker/tree/master/everscale)

## Exploring further development

In conclusion, this Proof of Concept (POC) project has potential for further improvement. Notably, there's room for enhancing aesthetics by concealing wires, and the opportunity to introduce additional functionalities.
