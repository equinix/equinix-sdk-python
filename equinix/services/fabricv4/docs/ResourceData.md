# ResourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Cloud Event asset href | [optional] 
**uuid** | **str** | Cloud Event asset uuid | [optional] 
**type** | **str** | Cloud Event asset type | [optional] 
**name** | **str** | Cloud Event asset name | [optional] 
**state** | **str** | Cloud Event asset state | [optional] 
**operation** | [**OperationalStatus**](OperationalStatus.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.resource_data import ResourceData

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceData from a JSON string
resource_data_instance = ResourceData.from_json(json)
# print the JSON string representation of the object
print(ResourceData.to_json())

# convert the object into a dict
resource_data_dict = resource_data_instance.to_dict()
# create an instance of ResourceData from a dict
resource_data_from_dict = ResourceData.from_dict(resource_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


