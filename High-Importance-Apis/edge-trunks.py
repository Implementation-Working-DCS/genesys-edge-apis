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
edge_id = 'edge_id_example' # str | Filter by Edge Ids (optional)
trunk_base_id = 'trunk_base_id_example' # str | Filter by Trunk Base Ids (optional)
trunk_type = 'trunk_type_example' # str | Filter by a Trunk type (optional)

try:
    # Get the list of available trunks.
    api_response = api_instance.get_telephony_providers_edges_trunks(page_number=page_number, page_size=page_size, sort_by=sort_by, sort_order=sort_order, edge_id=edge_id, trunk_base_id=trunk_base_id, trunk_type=trunk_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyProvidersEdgeApi->get_telephony_providers_edges_trunks: %s\n" % e)


'''
curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges/trunks' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'
'''