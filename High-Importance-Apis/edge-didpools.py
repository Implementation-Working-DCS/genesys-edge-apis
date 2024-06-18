import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configurar OAuth2 access token para autenticar: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'your_access_token'
# Tambien se puede usar get_client_credentials_token(...), get_saml2bearer_token(...), get_code_authorization_token(...) o get_pkce_token(...)

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi();
page_size = 25 # int | Page size (optional) (default to 25)
page_number = 1 # int | Page number (optional) (default to 1)
sort_by = 'number' # str | Sort by (optional) (default to 'number')
id = ['id_example'] # list[str] | Filter by a specific list of ID's (optional)

try:
    # Optener la lista de los didtools
    api_response = api_instance.get_telephony_providers_edges_didpools(page_size=page_size, page_number=page_number, sort_by=sort_by, id=id)
    pprint(api_response)
except ApiException as e:
    print("Error al llamar a la lista de TelephonyProvidersEdgeApi->get_telephony_providers_edges_didpools: %s\n" % e)

'''
Tambien se puede realizar mediante un curl:

curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges/didpools' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'

'''

'''
Un DID le permite a la compañía asignar un número personal para cada empleado, 
sin la necesidad de una línea telefónica física separada, se conecte al PBX. 
De esta forma, el tráfico telefónico puede ser separado y administrado más fácilmente.
'''