#!/usr/bin/python
"""
Summary: My Python K5 API Wrapper library
These example K5 API calls have been developed in python 2.7X to help K5 users understand how they can consume the Fujitsu K5 API.

The function documentation has been auto-generated and needs to be reviewed - don't believe every comment that you read - read the code :) 

Author: Miguel Angel Diego & Graham Land
Date: 22/01/2018

"""

import requests
import sys
import json
from k5contractsettingsV10 import *
import random
import string

def get_globally_scoped_token(adminUser, adminPassword, contract,
                              defaultid, region):
    """Get a global project scoped auth token

    Returns:
        Python Object: Globally Project Scoped Object
        Containing a Catalog List in the Body

    Args:
        adminUser (string): Administrative user name
        adminPassword (string): Password for above user
        contract (string): Contract name
        defaultid (string): Default project
        region (string): Unused, need to remove at a later date
    """
    identityURL = 'https://identity.gls.cloud.global.fujitsu.com/v3/auth/tokens'
    try:
        response = requests.post(identityURL,
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'},
                                 json={"auth":
                                         {"identity":
                                          {"methods": ["password"], "password":
                                           {"user":
                                           {"domain":
                                               {"name": contract},
                                            "name": adminUser,
                                            "password": adminPassword
                                            }}},
                                          "scope":
                                          {"project":
                                           {"id": defaultid
                                           }}}})
        return response
    except:
        return "Global Token Error"

def get_globally_rescoped_token(globaltoken, defaultid):
    """Summary - Get a global project scoped auth token

    Returns:
        STRING: Globally Scoped Object

    Args:
        globaltoken (string): valid global token
        defaultid (string): default projct id
    """
    identityURL = 'https://identity.gls.cloud.global.fujitsu.com/v3/auth/tokens'
    try:
        response = requests.post(identityURL,
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'},
                                 json={
                                     "auth": {
                                         "identity": {
                                             "methods": [
                                                 "token"
                                             ],
                                             "token": {
                                                 "id": globaltoken
                                             }
                                         },
                                         "scope": {
                                             "project": {
                                                 "id": defaultid
                                             }
                                         }
                                     }
                                 })
        return response
    except:
        return "Global Rescope Token Error"

def get_re_unscoped_token(k5token, region):
    """Summary - Get a regional unscoped auth token

    Returns:
        Object: Regionally Scoped Project  Token

    Args:
        k5token (TYPE): valid regional token
        region (TYPE): region
    """
    identityURL = 'https://identity.' + region + \
        '.cloud.global.fujitsu.com/v3/auth/tokens'
    tokenbody = {
        "auth": {
            "identity": {
                "methods": [
                    "token"
                ],
                "token": {
                    "id": k5token
                }
            },
        }
    }
    try:
        response = requests.post(identityURL,
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'},
                                 json=tokenbody)
        return response
    except:
        return 'Regional Re-Scoping Failure'

def get_rescoped_token(k5token, projectid, region):
    """Get a regional project token - rescoped

    Returns:
        STRING: Regionally Scoped Project  Token

    Args:
        k5token (TYPE): valid regional token
        projectid (TYPE): project id to scope to
        region (TYPE): k5 region
    """
    identityURL = 'https://identity.' + region + \
        '.cloud.global.fujitsu.com/v3/auth/tokens'
    try:
        response = requests.post(identityURL,
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'},
                                 json={
                                     "auth": {
                                         "identity": {
                                             "methods": [
                                                 "token"
                                             ],
                                             "token": {
                                                 "id": k5token
                                             }
                                         },
                                         "scope": {
                                             "project": {
                                                 "id": projectid
                                             }
                                         }
                                     }
                                 })

        return response
    except:
        return 'Regional Project Rescoping Failure'

def get_scoped_token(adminUser, adminPassword, contract, projectid, region):
    """Summary - Get a regional project scoped  token using a username and password

    Returns:
        Object: Regionally Scoped Project  Token Object

    Args:
        adminUser (TYPE): username
        adminPassword (TYPE): password
        contract (TYPE): contract name
        projectid (TYPE): project id
        region (TYPE): region
    """
    identityURL = 'https://identity.' + region + \
        '.cloud.global.fujitsu.com/v3/auth/tokens'

    try:
        response = requests.post(identityURL,
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'},
                                 json={"auth":
                                         {"identity":
                                          {"methods": ["password"], "password":
                                           {"user":
                                           {"domain":
                                               {"name": contract},
                                            "name": adminUser,
                                            "password": adminPassword
                                            }}},
                                          "scope":
                                          {"project":
                                           {"id": projectid
                                            }}}})

        return response
    except:
        return 'Regional Project Token Scoping Failure'

def get_unscoped_token(adminUser, adminPassword, contract, region):
    """Get a regional unscoped  token with username and password

    Returns:
        TYPE: Regional UnScoped Token Object

    Args:
        adminUser (TYPE): username
        adminPassword (TYPE): password
        contract (TYPE): k5 contract name
        region (TYPE): k5 region
    """
    identityURL = 'https://identity.' + region + \
        '.cloud.global.fujitsu.com/v3/auth/tokens'
    try:
        response = requests.post(identityURL,
                                 headers={'Content-Type': 'application/json',
                                          'Accept': 'application/json'},
                                 json={"auth":
                                       {"identity":
                                        {"methods": ["password"], "password":
                                         {"user":
                                            {"domain":
                                             {"name": contract},
                                                "name": adminUser,
                                                "password": adminPassword
                                             }}}}})
        return response
    except:
        return 'Regional Unscoped Token Failure'

def get_unscoped_idtoken(adminUser, adminPassword, contract):
    """Summary - Get a central identity portal token

    Returns:
        TYPE: Central Identity Token Header

    Args:
        adminUser (TYPE): k5 admin name
        adminPassword (TYPE): k5 password
        contract (TYPE): k5 contract
    """
    try:
        response = requests.post('https://auth-api.jp-east-1.paas.cloud.global.fujitsu.com/API/paas/auth/token',
                                 headers={'Content-Type': 'application/json'},
                                 json={"auth":
                                       {"identity":
                                        {"password":
                                         {"user":
                                          {"contract_number": contract,
                                           "name": adminUser,
                                           "password": adminPassword
                                           }}}}})

        return response.headers['X-Access-Token']
    except:
        return 'ID Token Failure'
