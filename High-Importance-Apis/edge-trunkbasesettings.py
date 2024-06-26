import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'your_access_token'
# or use get_client_credentials_token(...), get_saml2bearer_token(...), get_code_authorization_token(...) or get_pkce_token(...)

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi();
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
sort_by = 'name' # str | Value by which to sort (optional) (default to 'name')
sort_order = 'ASC' # str | Sort order (optional) (default to 'ASC')
recording_enabled = True # bool | Filter trunks by recording enabled (optional)
ignore_hidden = True # bool | Set this to true to not receive trunk properties that are meant to be hidden or for internal system usage only. (optional)
managed = True # bool | Filter by managed (optional)
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)
name = 'name_example' # str | Name of the TrunkBase to filter by (optional)

try:
    # Get Trunk Base Settings listing
    api_response = api_instance.get_telephony_providers_edges_trunkbasesettings(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, recording_enabled=recording_enabled, ignore_hidden=ignore_hidden, managed=managed, expand=expand, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunkbasesettings: %s\n" % e)

'''
curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges/trunkbasesettings' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'
'''