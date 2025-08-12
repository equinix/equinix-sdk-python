# MetroConnectPostRequest

Create Metro Connect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Metro Connect Type | 
**bandwidth** | **int** | Bandwidth in Mbps | 
**connectivity_destination_type** | [**MetroConnectPostRequestConnectivityDestinationType**](MetroConnectPostRequestConnectivityDestinationType.md) |  | 
**a_side** | [**MetroConnectASide**](MetroConnectASide.md) |  | 
**z_side** | [**MetroConnectZSide**](MetroConnectZSide.md) |  | 
**order** | [**MetroConnectOrder**](MetroConnectOrder.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_connect_post_request import MetroConnectPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetroConnectPostRequest from a JSON string
metro_connect_post_request_instance = MetroConnectPostRequest.from_json(json)
# print the JSON string representation of the object
print(MetroConnectPostRequest.to_json())

# convert the object into a dict
metro_connect_post_request_dict = metro_connect_post_request_instance.to_dict()
# create an instance of MetroConnectPostRequest from a dict
metro_connect_post_request_from_dict = MetroConnectPostRequest.from_dict(metro_connect_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


