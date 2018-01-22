#!/usr/bin/python
"""
Summary: My Python K5 API Wrapper KeyPair library
These example K5 API calls have been developed in python 2.7X to help K5 users understand how they can consume the Fujitsu K5 API.

The function documentation has been auto-generated and needs to be reviewed - don't believe every comment that you read - read the code :) 

Author: Miguel Angel Diego & Graham Land
Date: 22/01/2018

"""

from k5APIwrappersV18 import *

def list_keypairs(k5token, project_id, region):
    """Summary - list  K5 project keypairs

    Args:
        k5token (TYPE): valid regional domain scoped token
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object

    Deleted Parameters:
        userid(TYPE): K5 user id
    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/os-keypairs'
        response = requests.get(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())

def show_keypair(k5token, keypair_name, project_id, region):
    """Summary - show  K5 project keypair details

    Args:
        k5token (TYPE): valid regional domain scoped token
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object

    Deleted Parameters:
        userid(TYPE): K5 user id
    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/os-keypairs/' + keypair_name
        response = requests.get(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())


def delete_keypair(k5token, keypair_name, project_id, region):
    """Summary - show  K5 project keypair details

    Args:
        k5token (TYPE): valid regional domain scoped token
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object

    Deleted Parameters:
        userid(TYPE): K5 user id
    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/os-keypairs/' + keypair_name
        response = requests.delete(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())


def create_keypair(k5token, keypair_name, project_id, az, region):
    """Summary - Create  K5 project keypair

    Args:
        k5token (TYPE): valid regional domain scoped token
        keypair_name: name of ssh key pair
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object

    Deleted Parameters:
        userid(TYPE): K5 user id
    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/os-keypairs'
        response = requests.post(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'},
                                json={
                                    "keypair": {
                                        "name": keypair_name,
                                        "availability_zone": az
                                        }})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())
