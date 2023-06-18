#!/usr/bin/env python3
"""
Script that downloads backup files from Tasmota Devices as listed in the config file
"""

__author__ = "saurabh Datta"
__version__ = "0.1.0"
__license__ = "MIT"

import json
import urllib.request

import os
curr_dir = os.path.join(os.path.dirname(__file__))
print('script dir: ', curr_dir)
config_file = (curr_dir + '/devices_list.json')
print(config_file)

import subprocess




def download_config(_config_file):
    """ Querry and download current configs from device addresses """
    counter = 0
    with open(_config_file) as json_file:
        data = json.load(json_file)
        # print(json.dumps(data, indent=4, sort_keys=True))
        for device in data['devices']:
            counter += 1
            # print(device["name"], device["addr"])
            url = cmd = 'http://' + device['addr'] + '/dl'
            file_name = curr_dir + '/backups/' + device['name'] + '.dmp'
            print('[' + str(counter) + '] ' + 'Downloading current config from: ' + url + ' as ' + file_name)
            urllib.request.urlretrieve(url, file_name)

def push_to_git():
    """ Pushes everything to the git """
    os.system('git add .')
    os.system('git commit -m \"latest backup\"')
    os.system('git status')
    os.system('git push -u origin main')

def main():
    """ Main entry point of the app """
    download_config(config_file)
    push_to_git()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
