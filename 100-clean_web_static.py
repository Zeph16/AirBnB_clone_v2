#!/usr/bin/python3
""" Deletes the least recent input number of versions locally and remotely """
from fabric.api import *


env.hosts = ['34.229.64.128', '3.238.228.37']
env.user = "ubuntu"


def do_clean(number=0):
    """ Deletes folders/archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
