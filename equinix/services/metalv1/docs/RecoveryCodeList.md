# RecoveryCodeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**recovery_codes** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.recovery_code_list import RecoveryCodeList

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryCodeList from a JSON string
recovery_code_list_instance = RecoveryCodeList.from_json(json)
# print the JSON string representation of the object
print(RecoveryCodeList.to_json())

# convert the object into a dict
recovery_code_list_dict = recovery_code_list_instance.to_dict()
# create an instance of RecoveryCodeList from a dict
recovery_code_list_form_dict = recovery_code_list.from_dict(recovery_code_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


