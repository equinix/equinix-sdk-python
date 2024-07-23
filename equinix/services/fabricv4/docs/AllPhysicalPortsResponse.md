# AllPhysicalPortsResponse

GET All Physical Ports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[PhysicalPort]**](PhysicalPort.md) | GET All Physical Ports | [optional] 

## Example

```python
from equinix.services.fabricv4.models.all_physical_ports_response import AllPhysicalPortsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllPhysicalPortsResponse from a JSON string
all_physical_ports_response_instance = AllPhysicalPortsResponse.from_json(json)
# print the JSON string representation of the object
print(AllPhysicalPortsResponse.to_json())

# convert the object into a dict
all_physical_ports_response_dict = all_physical_ports_response_instance.to_dict()
# create an instance of AllPhysicalPortsResponse from a dict
all_physical_ports_response_form_dict = all_physical_ports_response.from_dict(all_physical_ports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


