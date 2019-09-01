LED aPI
==========

|Build Status| |Documentation Status| |GitHub|

This module aims to provide a simple way to manage a couple
of colored LEDs through a Raspberry Pi's GPIO and a REST API.

   **Note:** This setup is mainly for **fun** usage.

Installation proccess
---------------------

Download sources, unzip, goes to sources-folder.

Installation
~~~~~~~~~~~~

Use the ``setup.py`` using PIP:

.. code:: bash

   pip install .

Configuration
~~~~~~~~~~~~~

Prepare configuration files in your home dir:

.. code:: bash

   mkdir -p ~/.led-api
   cp ./logging.json ~/.led-api/
   cp ./led_config.json ~/.led-api/

The content of the ``led_config.json`` **must** be customized
depending on the GPIO PIN setup you want to use.

For example:

.. code:: json

  {
    "white": 4,
    "blue": 17,
    "green": 27,
    "yellow": 22,
    "red": 5
  }

You can use the ``pinout`` command of ``gpiozero`` (as explained here
`raspberrypi.org`_) to get the current GPIO PIN numbers:

.. code:: bash

   sudo pip install gpiozero
   pinout

Or the useful `pinout.xyz`_ web site.

Usage
-----

LED API
~~~~~~~

The LED API use the ``flask``/``flask_restplus`` module to provide
API and Swagger documentation.

To run the developpement server:

.. code:: bash

   led-api

Join the ``http://<your_IP_address>:5000`` URL to get the swagger
interface.


.. _raspberrypi.org: https://www.raspberrypi.org/documentation/usage/gpio/
.. _pinout.xyz: https://pinout.xyz/#

.. |Build Status| image:: https://travis-ci.org/lrivallain/led-api.svg?branch=master
   :target: https://travis-ci.org/lrivallain/led-api
.. |Documentation Status| image:: https://readthedocs.org/projects/led-api/badge/?version=latest
   :target: https://led-api.readthedocs.io/en/latest/?badge=latest
.. |GitHub| image:: https://img.shields.io/github/license/lrivallain/led-api