from .base import *

OAUTH2IO_HOST = "https://dev.bluebutton.cms.fhirservice.net"
OAUTH2_PROVIDER_NAME = "CMS"

SOCIAL_AUTH_OAUTH2IO_KEY = 'test_app'
SOCIAL_AUTH_OAUTH2IO_SECRET = 'some_secret'

# this is the client id of the application used to obtain tokens
# with the password flow in the integration tests.
# the app is defined in the staging server: http://oauth.npi.io
TEST_INTEGRATION_CLIENT_ID = 'test_app'
TEST_INTEGRATION_USERNAME = 'sometestuser'
TEST_INTEGRATION_PASSWORD = 'somepassword'

TEST_INTEGRATION_READ_CLIENT_ID = 'test_app_read'
TEST_INTEGRATION_WRITE_CLIENT_ID = 'test_app_write'

# this env variable is needed by oauthlib to disable the SSL
# check while testing, because the testing server doesn't use SSL
# import os
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
