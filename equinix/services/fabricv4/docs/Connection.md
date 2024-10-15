# Connection

Connection specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [optional] [readonly] 
**type** | [**ConnectionType**](ConnectionType.md) |  | 
**uuid** | **str** | Equinix-assigned connection identifier | [optional] 
**name** | **str** | Customer-provided connection name | 
**description** | **str** | Customer-provided connection description | [optional] 
**state** | [**ConnectionState**](ConnectionState.md) |  | [optional] 
**change** | [**Change**](Change.md) |  | [optional] 
**operation** | [**ConnectionOperation**](ConnectionOperation.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**bandwidth** | **int** | Connection bandwidth in Mbps | 
**geo_scope** | [**GeoScopeType**](GeoScopeType.md) |  | [optional] 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | [optional] 
**is_remote** | **bool** | Connection property derived from access point locations | [optional] 
**direction** | [**ConnectionDirection**](ConnectionDirection.md) |  | [optional] 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 
**additional_info** | [**List[ConnectionSideAdditionalInfo]**](ConnectionSideAdditionalInfo.md) | Connection additional information | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_form_dict = connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


