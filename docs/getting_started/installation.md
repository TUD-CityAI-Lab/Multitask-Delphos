# Installation

Delphos is currently under active development. The best way to use it is by cloning the repository and installing the user library locally.

## Prerequisites
- Python 3.9+
- [R](https://www.r-project.org/) and the [Apollo package](http://www.apollochoicemodelling.com/) (required for the estimation environment)

## Installing the User Library

To use pre-trained Delphos agents for assisted specification, you only need the `delphos` user library.

```bash
git clone --recurse-submodules https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
cd Multitask-Delphos/components/delphos
pip install -e .
```

## Installing for Training Development

If you intend to train new agents or modify the RL machinery, install the training component.

```bash
git clone https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
git submodule update --init --recursive
cd Multitask-Delphos/components/delphos-training
pip install -r requirements.txt
```
