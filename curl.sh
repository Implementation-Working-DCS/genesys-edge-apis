# Para pedir el token usando tu mismo curl:
# Envio:
curl --insecure -X POST https://login.cac1.pure.cloud/oauth/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials" -u "(ClientID):(Secret))"


curl -X GET https://api.cac1.pure.cloud/api/v2/telephony/providers/edges -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxx" -H "Content-Type: application/json"

PARA OBTENER LOS TRUNKS
curl -X GET https://api.cac1.pure.cloud/api/v2/telephony/providers/edges/trunks -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxx" -H "Content-Type: application/json"

DEL QUERY ANTERIOR POR EJEMPLO EXTRAIGO UN TRUNK:
  "id": "3ceb3bfd-8ec4-486b-bc90-9e24b2668bff",
  "name": "Caja_1 Trunk 6702759d-0407-4286-92d8-d94a95248397",



curl -X GET https://api.cac1.pure.cloud/api/v2/telephony/providers/edges/trunks/3ceb3bfd-8ec4-486b-bc90-9e24b2668bff -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" -H "Content-Type: application/json"


curl -X GET https://api.cac1.pure.cloud/api/v2/telephony/providers/edges/trunks/3ceb3bfd-8ec4-486b-bc90-9e24b2668bff/metrics -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxx" -H "Content-Type: application/json"  

