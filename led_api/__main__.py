#!/usr/bin/env python
from flask import Flask, request
from flask_restplus import Api, Resource, fields, abort
from .utils import init_logger
from gpiozero import LED
import os
import json


import logging
logger = logging.getLogger(__name__)

led_setup = {}

app = Flask(__name__)
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
app.config.SWAGGER_UI_OPERATION_ID = True
app.config.SWAGGER_UI_REQUEST_DURATION = True
api = Api(
    app,
    version='1.0',
    title='LED APi',
    description='Manage colored LEDs through Raspberry Pi GPIO',
)
ns_col = api.namespace('colors', description='Manage LED by colors')

# describe models
color_request = api.model('Change the status of a colored LED', {
    'on': fields.Boolean(
        required=True,
        description='Start or stop LED'
    ),
    'blink': fields.Boolean(
        required=False,
        description='Start LED with a blink configuration'
    )
})
message_op = api.model('Response message regarding the current request', {
    'message': fields.String(
        description='Description of the response made to the request.'
    )
})

@ns_col.route('/reset')
class Reset(Resource):
    """Reset all the LED to default status.
    """

    @ns_col.marshal_with(message_op)
    def post(self):
        """Reset all the LED to default status.
        """
        logger.info(f"Reset requested")
        for led in led_setup.keys():
            if led != 'white':
                led_setup[led].off()
        return {"message": "Reset request was successfully applied."}


@ns_col.route('/<color>')
@ns_col.param('color', "LED color")
class Colors(Resource):
    """Set and get the status for the LEDs.
    """

    # #@ns_cm.marshal_with(machine_status) #TODO
    # def get(self, color):
    #     """Get the current status of a colored LED.
    #     """
    #     logger.info("Current status of a colored LED is requested")
    #     return {
    #         #TODO
    #     }

    @ns_col.marshal_with(message_op)
    @ns_col.expect(color_request)
    def post(self, color):
        """Update the state of a colored LED.
        """
        if not led_setup.get(color):
            abort(404, f"Unconfigured color: {color}")
        req_on = request.json.get('on', False) # default is off command
        re_blink = request.json.get('blink', False) # default is no blink
        logger.info(f"Update of status of colored LED {color}")
        if req_on:
            if re_blink:
                led_setup[color].blink(on_time=.5, off_time=.5)
            else:
                led_setup[color].on()
        else:
            led_setup[color].off()
        return {"message": "Request was successfully applied."}


def main():
    """Execute the LED APi.
    """
    global led_setup
    init_logger()
    with open(os.path.expanduser("~/.led-api/led_config.json"), "r", encoding="utf-8") as fd:
        led_setup = json.load(fd)
    # swith all off
    for led in led_setup.keys():
        led_setup[led] = LED(led_setup[led])
        led_setup[led].off()
    # switch white on to indicate that the API is running
    led_setup['white'].on()
    logger.info("Starting the LED APi...")
    app.run(debug=False, host='0.0.0.0')
    # leaving...
    led_setup['white'].off()

if __name__ == '__main__':
    main()