# AllPortsResponse

GET All User Port Across Fabric Metros

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Port]**](Port.md) | GET All User Port Across Fabric Metros | [optional] 

## Example

```python
from equinix.services.fabricv4.models.all_ports_response import AllPortsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllPortsResponse from a JSON string
all_ports_response_instance = AllPortsResponse.from_json(json)
# print the JSON string representation of the object
print(AllPortsResponse.to_json())

# convert the object into a dict
all_ports_response_dict = all_ports_response_instance.to_dict()
# create an instance of AllPortsResponse from a dict
all_ports_response_form_dict = all_ports_response.from_dict(all_ports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


