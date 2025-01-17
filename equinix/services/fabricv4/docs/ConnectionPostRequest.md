# ConnectionPostRequest

Create connection post request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConnectionType**](ConnectionType.md) |  | 
**name** | **str** | Customer-provided connection name | 
**order** | [**Order**](Order.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | 
**bandwidth** | **int** | Connection bandwidth in Mbps | 
**geo_scope** | [**GeoScopeType**](GeoScopeType.md) |  | [optional] 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | [optional] 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**project** | [**Project**](Project.md) |  | [optional] 
**additional_info** | [**List[ConnectionSideAdditionalInfo]**](ConnectionSideAdditionalInfo.md) | Connection additional information | [optional] 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 
**end_customer** | [**EndCustomer**](EndCustomer.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_post_request import ConnectionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPostRequest from a JSON string
connection_post_request_instance = ConnectionPostRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionPostRequest.to_json())

# convert the object into a dict
connection_post_request_dict = connection_post_request_instance.to_dict()
# create an instance of ConnectionPostRequest from a dict
connection_post_request_from_dict = ConnectionPostRequest.from_dict(connection_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


