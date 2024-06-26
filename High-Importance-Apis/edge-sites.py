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
sort_by = 'name' # str | Sort by (optional) (default to 'name')
sort_order = 'ASC' # str | Sort order (optional) (default to 'ASC')
name = 'name_example' # str | Name (optional)
location_id = 'location_id_example' # str | Location Id (optional)
managed = True # bool | Filter by managed (optional)
expand = ['expand_example'] # list[str] | Fields to expand in the response, comma-separated (optional)

try:
    # Get the list of Sites.
    api_response = api_instance.get_telephony_providers_edges_sites(page_size=page_size, page_number=page_number, sort_by=sort_by, sort_order=sort_order, name=name, location_id=location_id, managed=managed, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_sites: %s\n" % e)

'''
curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges/sites' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'
'''