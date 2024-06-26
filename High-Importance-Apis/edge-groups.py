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
name = 'name_example' # str | Name (optional)
sort_by = 'name' # str | Sort by (optional) (default to 'name')
managed = True # bool | Filter by managed (optional)

try:
    # Get the list of edge groups.
    api_response = api_instance.get_telephony_providers_edges_edgegroups(page_size=page_size, page_number=page_number, name=name, sort_by=sort_by, managed=managed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_edgegroups: %s\n" % e)

'''
curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges/edgegroups' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'
'''