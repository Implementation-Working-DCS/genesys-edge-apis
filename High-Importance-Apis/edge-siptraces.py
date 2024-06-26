import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'your_access_token'
# or use get_client_credentials_token(...), get_saml2bearer_token(...), get_code_authorization_token(...) or get_pkce_token(...)

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi();
date_start = '2013-10-20T19:20:30+01:00' # datetime | Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
date_end = '2013-10-20T19:20:30+01:00' # datetime | End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
call_id = 'call_id_example' # str | unique identification of the placed call (optional)
to_user = 'to_user_example' # str | User to who the call was placed (optional)
from_user = 'from_user_example' # str | user who placed the call (optional)
conversation_id = 'conversation_id_example' # str | Unique identification of the conversation (optional)

try:
    # Fetch SIP metadata
    api_response = api_instance.get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces: %s\n" % e)


'''
curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/siptraces' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'
'''