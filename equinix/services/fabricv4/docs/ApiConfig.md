# ApiConfig

Configuration for API based Integration for Service Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_available** | **bool** | Setting indicating whether the API is available (true) or not (false). | [optional] [default to False]
**integration_id** | **str** |  | [optional] 
**equinix_managed_port** | **bool** | Setting indicating that the port is managed by Equinix (true) or not (false). | [optional] [default to False]
**equinix_managed_vlan** | **bool** | Setting indicating that the VLAN is managed by Equinix (true) or not (false). | [optional] [default to False]
**allow_over_subscription** | **bool** | Setting showing that oversubscription support is available (true) or not (false). The default is false. Oversubscription is the sale of more than the available network bandwidth. This practice is common and legitimate. After all, many customers use less bandwidth than they&#39;ve purchased. And network users don&#39;t consume bandwidth all at the same time. The leftover bandwidth can be sold to other customers. When demand surges, operational and engineering resources can be shifted to accommodate the load.  | [optional] [default to False]
**over_subscription_limit** | **int** | A cap on oversubscription. | [optional] [default to 1]
**bandwidth_from_api** | **bool** |  | [optional] [default to False]

## Example

```python
from equinix.services.fabricv4.models.api_config import ApiConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfig from a JSON string
api_config_instance = ApiConfig.from_json(json)
# print the JSON string representation of the object
print(ApiConfig.to_json())

# convert the object into a dict
api_config_dict = api_config_instance.to_dict()
# create an instance of ApiConfig from a dict
api_config_form_dict = api_config.from_dict(api_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


