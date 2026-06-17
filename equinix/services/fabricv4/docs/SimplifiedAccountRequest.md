# SimplifiedAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** | Account number | 

## Example

```python
from equinix.services.fabricv4.models.simplified_account_request import SimplifiedAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedAccountRequest from a JSON string
simplified_account_request_instance = SimplifiedAccountRequest.from_json(json)
# print the JSON string representation of the object
print(SimplifiedAccountRequest.to_json())

# convert the object into a dict
simplified_account_request_dict = simplified_account_request_instance.to_dict()
# create an instance of SimplifiedAccountRequest from a dict
simplified_account_request_from_dict = SimplifiedAccountRequest.from_dict(simplified_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


