import os


# Path to directory project
DIR_PROJECT = os.path.dirname(__file__)

# API-key SuperJob.ru
NAME_API_KEY_SUPER_JOB = 'API_KEY_SuperJob'
API_KEY_SJ = os.getenv('API_KEY_SuperJob')

# API-key HeadHunter.ru
NAME_API_KEY_CLIENT_ID = 'API_KEY_HeadHunter_client_ID'
API_CLIENT_ID = os.getenv(NAME_API_KEY_CLIENT_ID)

NAME_API_KEY_SECRET = 'API_KEY_HeadHunter_secret'
API_CLIENT_SECRET = os.getenv(NAME_API_KEY_SECRET)
