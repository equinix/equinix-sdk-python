# NetworkPostRequest

Create Network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NetworkType**](NetworkType.md) |  | 
**name** | **str** | Customer-provided network name | 
**scope** | [**NetworkScope**](NetworkScope.md) |  | 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on network configuration or status changes | 

## Example

```python
from equinix.services.fabricv4.models.network_post_request import NetworkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPostRequest from a JSON string
network_post_request_instance = NetworkPostRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkPostRequest.to_json())

# convert the object into a dict
network_post_request_dict = network_post_request_instance.to_dict()
# create an instance of NetworkPostRequest from a dict
network_post_request_form_dict = network_post_request.from_dict(network_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


