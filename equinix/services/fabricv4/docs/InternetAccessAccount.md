# InternetAccessAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Account number | 
**href** | **str** | Account URL path | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_account import InternetAccessAccount

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessAccount from a JSON string
internet_access_account_instance = InternetAccessAccount.from_json(json)
# print the JSON string representation of the object
print(InternetAccessAccount.to_json())

# convert the object into a dict
internet_access_account_dict = internet_access_account_instance.to_dict()
# create an instance of InternetAccessAccount from a dict
internet_access_account_from_dict = InternetAccessAccount.from_dict(internet_access_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


