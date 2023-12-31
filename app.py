#!/usr/bin/env python3
"""
Script that downloads backup files from Tasmota Devices as listed in the config file
"""

__author__ = "saurabh Datta"
__version__ = "0.1.0"
__license__ = "MIT"

import time
from datetime import datetime
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
    print('Downloading current configs from tasmota devices ...')
    time.sleep(2)
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y-%H:%M:%S_")
    counter = 0
    with open(_config_file) as json_file:
        data = json.load(json_file)
        # print(json.dumps(data, indent=4, sort_keys=True))
        for device in data['devices']:
            counter += 1
            # print(device["name"], device["addr"])
            url = cmd = 'http://' + device['addr'] + '/dl'
            file_name = curr_dir + '/backups/' + dt_string + device['name'] + '.dmp'
            print('[' + str(counter) + '] ' + 'Downloading current config from: ' + url + ' as ' + file_name)
            try:
                urllib.request.urlretrieve(url, file_name)
            except Exception:
                print('host unreachable ...')
                continue

def push_to_git():
    """ Pushes everything to the git """
    print('\nPushing to git ...\n')
    time.sleep(2)
    os.system('git pull')
    os.system('git add .')
    os.system('git commit -m \"latest backup\"')
    os.system('git status')
    os.system('git push -u origin main')

def main():
    """ Main entry point of the app """
    # Remove old files
    print("Removing old files ...")
    os.system('rm /home/pi/IoTDevicesBackup/backups/*.dmp')
    time.sleep(2)
    
    download_config(config_file)
    push_to_git()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
