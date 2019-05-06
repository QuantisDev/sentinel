import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from quantisnet_config import QuantisnetConfig
from quantisnetd import QuantisnetDaemon

def test_quantisnetd():
    config_text = QuantisnetConfig.slurp_config_file(config.quantisnet_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'000007cc671fb0663ccb1c9141e06d04152e9a5a1e8c0e1fdf81b283267faca7'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'000007cc671fb0663ccb1c9141e06d04152e9a5a1e8c0e1fdf81b283267faca7'

    creds = QuantisnetConfig.get_rpc_creds(config_text, network)
    quantisnetd = QuantisnetDaemon(**creds)
    assert quantisnetd.rpc_command is not None

    assert hasattr(quantisnetd, 'rpc_connection')

    # Quantisnet testnet block 0 hash == 00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c
    # test commands without arguments
    info = quantisnetd.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert quantisnetd.rpc_command('getblockhash', 0) == genesis_hash
