# GatewayTunnelSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**GatewayTunnelSortDirection**](GatewayTunnelSortDirection.md) |  | [optional] [default to GatewayTunnelSortDirection.DESC]
**var_property** | **str** | Possible field names to use on sorting:   * &#x60;/name&#x60; - Gateway Tunnel name   * &#x60;/uuid&#x60; - Gateway Tunnel uuid   * &#x60;/state&#x60; - Gateway Tunnel status   * &#x60;/changeLog/createdDateTime&#x60; - Date and time when change flow starts   * &#x60;/changeLog/updatedDateTime&#x60; - Date and time when change object is updated  | [optional] [default to '/changeLog/updatedDateTime']

## Example

```python
from equinix.services.fabricv4.models.gateway_tunnel_sort_criteria import GatewayTunnelSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayTunnelSortCriteria from a JSON string
gateway_tunnel_sort_criteria_instance = GatewayTunnelSortCriteria.from_json(json)
# print the JSON string representation of the object
print(GatewayTunnelSortCriteria.to_json())

# convert the object into a dict
gateway_tunnel_sort_criteria_dict = gateway_tunnel_sort_criteria_instance.to_dict()
# create an instance of GatewayTunnelSortCriteria from a dict
gateway_tunnel_sort_criteria_from_dict = GatewayTunnelSortCriteria.from_dict(gateway_tunnel_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


