from k5vm import *

def main():
    k5token = get_scoped_token(adminUser, adminPassword, contract, projectID, region).headers['X-Subject-Token']
    print k5token

    response = server_action(k5token, 'unshelve', 'null', '070e6151-12fe-444a-ac4d-f7fb05c0a0c2', projectID, region)

    print response

    response = server_action(k5token, 'shelve', 'null', '070e6151-12fe-444a-ac4d-f7fb05c0a0c2', projectID, region)

    print response

if __name__ == "__main__":
    main()