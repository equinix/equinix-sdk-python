# InterconnectPostRequest

Create Interconnect request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InterconnectPostRequestType**](InterconnectPostRequestType.md) |  | 
**name** | **str** | Customer-provided interconnect name | 
**description** | **str** | Customer-provided interconnect description | [optional] 
**location** | [**InterconnectLocationRequest**](InterconnectLocationRequest.md) |  | 
**package** | [**InterconnectPackage**](InterconnectPackage.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | 
**project** | [**Project**](Project.md) |  | 
**notifications** | [**List[InterconnectNotification]**](InterconnectNotification.md) | Preferences for notifications on interconnect configuration or status changes | 

## Example

```python
from equinix.services.fabricv4.models.interconnect_post_request import InterconnectPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectPostRequest from a JSON string
interconnect_post_request_instance = InterconnectPostRequest.from_json(json)
# print the JSON string representation of the object
print(InterconnectPostRequest.to_json())

# convert the object into a dict
interconnect_post_request_dict = interconnect_post_request_instance.to_dict()
# create an instance of InterconnectPostRequest from a dict
interconnect_post_request_from_dict = InterconnectPostRequest.from_dict(interconnect_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


