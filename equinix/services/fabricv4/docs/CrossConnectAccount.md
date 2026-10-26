# CrossConnectAccount

Account the Cross Connect belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** | Account number. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_account import CrossConnectAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectAccount from a JSON string
cross_connect_account_instance = CrossConnectAccount.from_json(json)
# print the JSON string representation of the object
print(CrossConnectAccount.to_json())

# convert the object into a dict
cross_connect_account_dict = cross_connect_account_instance.to_dict()
# create an instance of CrossConnectAccount from a dict
cross_connect_account_from_dict = CrossConnectAccount.from_dict(cross_connect_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


