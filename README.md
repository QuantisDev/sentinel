# QuantisNet Sentinel

An all-powerful toolset for QuantisNet.

Sentinel is an autonomous agent for persisting, processing and automating Quantis Network governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version 2.1.2 quantisnetd instance on each QuantisNet v2.1.2 masternode.

This guide covers installing Sentinel onto an existing v2.1.2 Masternode in Ubuntu 14.04 / 16.04.

## Installation - Linux

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv
    $ sudo apt-get install virtualenv

Make sure the local QuantisNet daemon running is at least version 20.102 (2010200)

    $ quantisnet-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/QuantisDev/sentinel && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### 4. Test the Configuration

Test the config by runnings all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with energid and the installation is complete

## Configuration

Path to the `quantisnet.conf` file can be specified in `sentinel.conf`:

    quantisnet_conf=/path/to/quantisnet.conf
    
## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

-----------------------------------------------------------------------------------------------------


## Installation - Windows

### 1. Downloading

Download [quansentinel.zip] located in this release, and extract the contents to a folder on your PC.

### 2. Configuration

Open sentinel.conf and adjust the line:

quantisnet_conf=C:\Users\YOURUSERNAME\AppData\Roaming\QuantisNetCore\quantisnet.conf

To point to your QuantisNetCore directory.

### 3. Check Wallet Config

Open quantisnet.conf and make sure it has at least:

rpcpassword=somepass
server=1
rpcport=13332
rpcconnect=127.0.0.1

Restart QuantisNet-QT and wait for it to sync.

### 4. Running

Run quansentinel

Press 1.


### License

Released under the MIT license, under the same terms as QuantisNet itself. See [LICENSE](LICENSE) for more info.
