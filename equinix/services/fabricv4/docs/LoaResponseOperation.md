# LoaResponseOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumers_count** | **int** | Number of consumers associated with this LOA. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_response_operation import LoaResponseOperation

# TODO update the JSON string below
json = "{}"
# create an instance of LoaResponseOperation from a JSON string
loa_response_operation_instance = LoaResponseOperation.from_json(json)
# print the JSON string representation of the object
print(LoaResponseOperation.to_json())

# convert the object into a dict
loa_response_operation_dict = loa_response_operation_instance.to_dict()
# create an instance of LoaResponseOperation from a dict
loa_response_operation_from_dict = LoaResponseOperation.from_dict(loa_response_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


