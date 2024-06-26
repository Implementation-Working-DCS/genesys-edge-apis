import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'your_access_token'
# or use get_client_credentials_token(...), get_saml2bearer_token(...), get_code_authorization_token(...) or get_pkce_token(...)

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi();
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'number' # str | Sort by (optional) (default to 'number')
sort_order = 'ASC' # str | Sort order (optional) (default to 'ASC')
phone_number = 'phone_number_example' # str | Filter by phoneNumber (optional)
owner_id = 'owner_id_example' # str | Filter by the owner of a phone number (optional)
did_pool_id = 'did_pool_id_example' # str | Filter by the DID Pool assignment (optional)
id = ['id_example'] # list[str] | Filter by a specific list of ID's (optional)

try:
    # Get a listing of DIDs
    api_response = api_instance.get_telephony_providers_edges_dids(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, phone_number=phone_number, owner_id=owner_id, did_pool_id=did_pool_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_dids: %s\n" % e)

'''
curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges/dids' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'
'''