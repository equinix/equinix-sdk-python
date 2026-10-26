# CrossConnectDiverse

Cross Connects returned by a diverse order. One item is returned per Cross Connect requested; a diverse pair returns the PRIMARY and the SECONDARY Cross Connect sharing one redundancy group. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CrossConnectResponse]**](CrossConnectResponse.md) | The Cross Connects the diverse order applies to. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_diverse import CrossConnectDiverse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectDiverse from a JSON string
cross_connect_diverse_instance = CrossConnectDiverse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectDiverse.to_json())

# convert the object into a dict
cross_connect_diverse_dict = cross_connect_diverse_instance.to_dict()
# create an instance of CrossConnectDiverse from a dict
cross_connect_diverse_from_dict = CrossConnectDiverse.from_dict(cross_connect_diverse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


