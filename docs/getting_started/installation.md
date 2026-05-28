# Installation

Delphos is currently under active development. The best way to use it is by cloning the repository and installing the user library locally.

## Prerequisites
- Python 3.9+
- [R](https://www.r-project.org/) and the [Apollo package](http://www.apollochoicemodelling.com/) (required for the estimation environment)

## Installing the User Library

To use pre-trained Delphos agents for assisted specification, you only need the `delphos` user library.

```bash
git clone https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
cd Multitask-Delphos/submodules/delphos-user
pip install -e .
```

## Installing for Development (Core)

If you intend to train new agents or modify the RL environment, you need to install the core repository.

```bash
git clone https://github.com/TUD-CityAI-Lab/Multitask-Delphos.git
git submodule update --init --recursive
cd Multitask-Delphos/submodules/delphos-core
pip install -r requirements.txt
pip install -e .
```
