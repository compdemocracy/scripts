import pandas as pd
from dotenv import load_dotenv
import requests
import os
import sys

load_dotenv('./.env')

CONVERSATION_ID = os.getenv('CONVERSATION_ID')
POLIS_USERNAME = os.getenv('POLIS_USERNAME')
POLIS_PASSWORD = os.getenv('POLIS_PASSWORD')
COMMENT_FILENAME = os.getenv('COMMENT_FILENAME')
POLIS_API_BASE_URL = os.getenv('POLIS_API_BASE_URL')
# Err on the side of performing a dry run
DRY_RUN = True if os.getenv('DRY_RUN').lower() != 'false' else False


def check():
    print(f'''
    Dry run: {DRY_RUN}
    Debate: {CONVERSATION_ID}
    Account: {POLIS_USERNAME}
    Polis API URL: {POLIS_API_BASE_URL}
    File: {COMMENT_FILENAME}
    ''')

    input("Is this ok? [Enter to continue]")
    print('')


def report(comment_id, result, statement):
    '''Standardise reporting'''
    try:
        comment_id_str = str(int(comment_id))
    except (ValueError, TypeError):
        comment_id_str = 'NaN'
    print(f"{comment_id_str}|{result}|{statement}")


def login(session):
    '''Logs into pol.is'''
    res = session.post(POLIS_API_BASE_URL + '/auth/login', json={
        'email': POLIS_USERNAME, 'password': POLIS_PASSWORD})
    if res.status_code != 200:
        print('Failed to login - quitting')
        sys.exit()


def main():
    '''The main script'''
    print(f'Reading {COMMENT_FILENAME} ...')

    new_statements = pd.read_csv(COMMENT_FILENAME)['new-comments']

    session = requests.Session()

    print('Getting a sign-in token ...')
    login(session)

    for statement in new_statements:
        comment_id = None
        result = 'Added'
        if not DRY_RUN:
            res = session.post(POLIS_API_BASE_URL + '/comments', json={
                'txt': statement, 'pid': 'mypid', 'conversation_id': CONVERSATION_ID, 'is_seed': 'true'})
            comment_id = res.json()['tid']
            if res.status_code != 200:
                result = f'Failed with status {res.status_code}'
        report(comment_id, result, statement)

    print('')
    print('Done')


if __name__ == '__main__':
    check()
    main()
