import requests
import json
import os
import sys

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
tenant_name = os.environ['TENANT']

#Change horizon_name for the value defined on your Openstack Cloud 
url_token = 'https://horizon_name:5000/v2.0/tokens"
url_tenants = 'https://horizon_name:5000/v2.0/tenants'


def get_token(username, password, tenant):

    """"

    This function will return a token that you will need for authentication

    Args:
        username: admin openstack user
        password: password of the admin user
        tenant: any of the existing tenants
    """

    json_payload = {"auth":{"tenantName":tenant_name,"passwordCredentials":{"username":username,"password":password}}}
    headers = {'content-type': 'application/json', 'accept': 'application/json'}
    output = requests.post(url= url_token , data=json.dumps(json_payload), headers=headers)
    return output.json()['access']['token']['id']

def get_tenants():

    """
    
    Returns:
        List of tenants already created

    """

    header_token = {}
    header_token['X-Auth-Token'] = get_token(username, password, tenant_name)
    tenants = requests.get(url_tenants, headers=header_token)
    list_of_tenants = []
    number_of_tenants = len(tenants.json()['tenants'])
    for tenant in range(number_of_tenants): 
        list_of_tenants.append(tenants.json()['tenants'][tenant]['name'])
    return list_of_tenants


list1 = get_tenants()

#Print a list of tenants 
print list1

