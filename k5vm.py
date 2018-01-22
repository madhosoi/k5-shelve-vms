#!/usr/bin/python
"""
Summary: My Python K5 API Wrapper Virtual Machine library
These example K5 API calls have been developed in python 2.7X to help K5 users understand how they can consume the Fujitsu K5 API.

The function documentation has been auto-generated and needs to be reviewed - don't believe every comment that you read - read the code :) 

Author: Miguel Angel Diego & Graham Land
Date: 22/01/2018

"""

from k5APIwrappersV18 import *

def list_vms(k5token, project_id, region):
    """Summary - list  K5 project vms

    Args:
        k5token (TYPE): valid regional domain scoped token
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object

    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/servers'
        response = requests.get(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())

def show_vm(k5token, vm_name, project_id, region):
    """Summary - show  K5 project vm details

    Args:
        k5token (TYPE): valid regional domain scoped token
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object
    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/servers/' + vm_name
        response = requests.get(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())


def delete_vm(k5token, vm_name, project_id, region):
    """Summary - show  K5 project vm details

    Args:
        k5token (TYPE): valid regional domain scoped token
        project_id (TYPE): Description
        region (TYPE): K5 region

    Returns:
        TYPE: http response object

    """

    try:

        serverURL = 'https://compute.' + region + \
            '.cloud.global.fujitsu.com/v2/' + project_id + '/servers/' + vm_name
        response = requests.delete(serverURL,
                                headers={
                                     'X-Auth-Token': k5token,
                                     'Content-Type': 'application/json',
                                     'Accept': 'application/json'})
        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())


def create_vm(k5token, name, imageid, flavorid, sshkey, sgname, az, volsize, networkid, projectid, region):
    """Summary

    Args:
        name (TYPE): Description

    Returns:
        TYPE: Description
    """
    serverURL = 'https://compute.' + region + '.cloud.global.fujitsu.com/v2/' + projectid + '/servers'
    try:


        response = requests.post(serverURL,
                                headers={'X-Auth-Token':k5token,'Content-Type': 'application/json','Accept':'application/json'},
                                json={"server": {

                                                 "name": name,
                                                 "security_groups":[{"name": sgname }],
                                                 "availability_zone":az,
                                                 "imageRef": imageid,
                                                 "flavorRef": flavorid,
                                                 "key_name": sshkey,
                                                 "block_device_mapping_v2": [{
                                                                               "uuid": imageid,
                                                                               "boot_index": "0",
                                                                               "device_name": "/dev/vda",
                                                                               "source_type": "image",
                                                                               "volume_size": volsize,
                                                                               "destination_type": "volume",
                                                                               "delete_on_termination": True
                                                                            }],
                                                 "networks": [{"uuid": networkid}],
                                                 "metadata": {"Example Custom Tag": "Finance Department"}
                                                }})

        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())

def server_action(k5token, actionname, actionvalue, serverid, projectid, region):
    """Summary

    Args:
        name (TYPE): Description

    Returns:
        TYPE: Description
    """
    serverURL = 'https://compute.' + region + '.cloud.global.fujitsu.com/v2/' + projectid + '/servers/' + serverid + '/action'
    try:


        response = requests.post(serverURL,
                                headers={'X-Auth-Token':k5token,'Content-Type': 'application/json','Accept':'application/json'},
                                json={ actionname : actionvalue })

        return response
    except:
        return ("\nUnexpected error:", sys.exc_info())