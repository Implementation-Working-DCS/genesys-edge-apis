import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configurar el access token para la autorizacion de PureCloud
PureCloudPlatformClientV2.configuration.access_token = 'your_access_token'
# Tambien se puede usar get_client_credentials_token(...), get_saml2bearer_token(...), get_code_authorization_token(...) o get_pkce_token(...)

# Crear una instancia para las clases de la api:
api_instance = PureCloudPlatformClientV2.TelephonyProvidersEdgeApi();
page_size = 25 # Numero entero | el tamaño de la pagina (opcional) (default = 25)
page_number = 1 # Numero entero | el numero de la pagina (opcional) (default = 1)
name = 'name_example' # Caracteres | Nombre (opcional)
site_id = 'site_id_example' # Caracteres | Filtra por site.id (opcional)
edge_group_id = 'edge_group_id_example' # Caracteres | Filtra por edgeGroup.id (opcional)
sort_by = 'name' # Caracteres | Ordena por nombre (opcional) (default = 'name')
managed = True # bool | Filtra por manejados (opcional)
show_cloud_media = True # bool | Muestra los  cloud media devices en los resultados (opcional) (default = True)

try:
    # Optiene la lista de edges
    api_response = api_instance.get_telephony_providers_edges(page_size=page_size, page_number=page_number, name=name, site_id=site_id, edge_group_id=edge_group_id, sort_by=sort_by, managed=managed, show_cloud_media=show_cloud_media)
    pprint(api_response)
except ApiException as e: #Error al optener la lista de edges.
    print("Ocurrio una exepcion cuando se llamo a los edges->get_telephony_providers_edges: %s\n" % e)

'''
Tambien se puede ejecutar mendiante un curl:

curl -X GET 'https://api.mypurecloud.com/api/v2/telephony/providers/edges' \
  -H 'Authorization: Bearer *******************' \
  -H 'Content-Type: application/json'

'''