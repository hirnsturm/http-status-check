#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Steve Lenz"
__copyright__ = "Copyright 2020"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Steve Lenz"
__email__ = "kontakt@steve-lenz"

import sys
from utility import output

# Check Python version
assert sys.version_info >= (3, 7), f'{output.Subject.ERROR} This script needs minimum Python 3.7!'

# Check requirements
try:
    import argparse
    import yaml
    import requests
except ImportError:
    print(
        f'{output.Subject.ERROR} Missing requirements! Install requirements with pip: pip3 install -r requirements.txt')
    sys.exit(1)


class HTTPStatusCheck:
    """
    Check multiple URL routes against an expected HTTP status code.
    """

    args = []
    configuration = []

    def __init__(self):
        """
        Initialization
        :return:
        """
        self.print_info()
        self.get_arguments()
        self.load_configuration()
        self.run_checks()
        print(f'{output.Subject.OK} Done.')

    def load_configuration(self):
        """
        Loads data from YAML configuration
        :return:
        """
        print(f'{output.Subject.INFO} Read configuration from {self.args.config}')
        self.configuration = yaml.safe_load(open(self.args.config))
        self.print_debug(self.configuration)

    def run_checks(self):
        """
        Runs access verification
        :return:
        """
        print(f'{output.Subject.INFO} Check routes against expected status code: {output.CliTextColor.GREEN}{self.configuration["expectedHttpStatusCode"]}{output.CliTextColor.ENDC}')
        for file in self.configuration['routes']:
            url = f'{self.configuration["domain"]}{file}'

            self.print_debug(f'Request {url}')

            try:
                request = requests.get(url)
            except requests.exceptions.RequestException as e:
                print(f'{output.Subject.ERROR}')
                raise SystemExit(e)

            self.print_debug(f'Response headers: {request.headers}')

            if self.configuration['expectedHttpStatusCode'] == request.status_code:
                print(f'{output.Subject.OK} {url} returns HTTP status {output.CliTextColor.GREEN}{request.status_code}{output.CliTextColor.ENDC}')
            else:
                print(f'{output.Subject.ERROR} {url} returns HTTP status {output.CliTextColor.RED}{request.status_code}{output.CliTextColor.ENDC}')

    def get_arguments(self):
        """
        Parses and returns script arguments
        :param self:
        :return:
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('--config',
                            help='Absolute path to config.yaml',
                            required=True,
                            type=str)
        parser.add_argument('--debug',
                            help='Enable debug output',
                            required=False,
                            action='store_true')
        self.args = parser.parse_args()

    def print_debug(self, content):
        """
        Prints debug output
        :param self:
        :param content:
        :return:
        """
        if self.args.debug:
            print(f'{output.Subject.DEBUG} {content}')

    def print_info(self):
        """
        Prints app information
        :return:
        """
        print(output.CliTextColor.BLUE)
        print('*****************************************')
        print('*                                       *')
        print('*           HTTP Status Check           *')
        print(f'*           {output.CliTextColor.ENDC}by {__author__}{output.CliTextColor.BLUE}               *')
        print('*                                       *')
        print('*****************************************')
        print(output.CliTextColor.ENDC)


#
# MAIN
#
if __name__ == "__main__":
    HTTPStatusCheck()
