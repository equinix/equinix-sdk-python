# ServiceTokenSide

Connection link protocol configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_point_selectors** | [**List[AccessPointSelector]**](AccessPointSelector.md) | List of AccessPointSelectors | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_token_side import ServiceTokenSide

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokenSide from a JSON string
service_token_side_instance = ServiceTokenSide.from_json(json)
# print the JSON string representation of the object
print(ServiceTokenSide.to_json())

# convert the object into a dict
service_token_side_dict = service_token_side_instance.to_dict()
# create an instance of ServiceTokenSide from a dict
service_token_side_from_dict = ServiceTokenSide.from_dict(service_token_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


