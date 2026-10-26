# CrossConnectRedundancy

Cross Connect Redundancy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Redundancy group identifier. When placing a diverse Cross Connect against an existing one, provide either this identifier or the serial number of the existing Cross Connect.  | [optional] 
**priority** | [**CrossConnectRedundancyPriority**](CrossConnectRedundancyPriority.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_redundancy import CrossConnectRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectRedundancy from a JSON string
cross_connect_redundancy_instance = CrossConnectRedundancy.from_json(json)
# print the JSON string representation of the object
print(CrossConnectRedundancy.to_json())

# convert the object into a dict
cross_connect_redundancy_dict = cross_connect_redundancy_instance.to_dict()
# create an instance of CrossConnectRedundancy from a dict
cross_connect_redundancy_from_dict = CrossConnectRedundancy.from_dict(cross_connect_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


