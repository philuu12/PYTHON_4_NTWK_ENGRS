#!/usr/bin/env python
"""
4. Use the PyEZ load() method to set the hostname of the SRX using set, conf
(curly brace), and XML formats.

After each load(), display the differences between the running config and
the candidate config. Additionally, perform at least one commit and
one rollback(0) in this program.

The committed hostname at the end of the program should be:  pynet-jnpr-srx1
"""

# Load Juniper PyEZ module
from jnpr.junos import Device
from getpass import getpass
from jnpr.junos.utils.config import Config

pwd = getpass()

# Create a Device instance
a_device = Device(host="50.76.53.27", user="pyclass", password=pwd)

# Establish a connection with Juniper device
a_device.open()

# Create a Config instance
cfg = Config(a_device)

# Lock the Juniper device while you are doing the config changes
cfg.lock()

# 1. Load config via load-set command
cfg.load("set system host-name juniper-test-name", format="set", merge=True)

# Show the differences between running-config and candidate config
print cfg.diff()

#cfg.commit()

# Rollback the candidate config changes
cfg.rollback(0)


# 2. Load new config via 'test_config.conf' file (using curly braces)
# Create test_config.conf file first in the currently-running Linux directory
cfg.load(path="test_config.conf", format="text", merge=True)

# Show the differences between running-config and candidate config
print cfg.diff()

cfg.rollback(0)


# 3. Load new config via 'test_config.xml' file (in XML format) 
# Create test_config.xml file first in the currently-running Linux directory
cfg.load(path="test_config.xml", format="xml", merge=True)

# Show the differences between running-config and candidate-config
print cfg.diff()

# commit will rollback the changes after 1 minute time interval specified below
cfg.commit(comment="Testing commit command", confirm=1) 



