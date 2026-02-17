# ResponseIncompleteDetails

Details about why the response is incomplete. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**ResponseIncompleteDetailsReason**](ResponseIncompleteDetailsReason.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.response_incomplete_details import ResponseIncompleteDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseIncompleteDetails from a JSON string
response_incomplete_details_instance = ResponseIncompleteDetails.from_json(json)
# print the JSON string representation of the object
print(ResponseIncompleteDetails.to_json())

# convert the object into a dict
response_incomplete_details_dict = response_incomplete_details_instance.to_dict()
# create an instance of ResponseIncompleteDetails from a dict
response_incomplete_details_from_dict = ResponseIncompleteDetails.from_dict(response_incomplete_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


