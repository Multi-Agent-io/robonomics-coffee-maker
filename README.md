# Robonomics Coffee

## About
"Robonomics coffee" - is a smart coffee machine integrated in  [Robonomics Network](https://robonomics.network/).
This project aims to show Robonomics potential in the IoT sphere by a real-world example. More info and tutorial may be
found in [Robonomcis Wiki](https://wiki.robonomics.network/docs/en/robonomics-coffee/)

## Installation and dualism

Generally, there are two blockchain networks used: 
[Robonomics Kusama Parachain](https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fkusama.rpc.robonomics.network%2F#/explorer) 
and [Everscale](https://net.ever.live/).

So, there are two different subprojects, that slightly differ in the income tracking patterns. Follow inner `READMEs` for more.

Also, for each subproject there is a generated `systemd service` file to be put in `/etc/systemd/system`.
**Edit script paths in them first** and then move these files.

```bash
sudo mv robonomics_coffee_maker_everscale.service /etc/systemd/system
sudo mv robonomics_coffee_maker_robonomics_kusama.service /etc/systemd/system
```