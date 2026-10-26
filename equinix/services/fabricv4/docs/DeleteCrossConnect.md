# DeleteCrossConnect

Delete Cross Connect request. Carries the removal schedule together with the notification and order details to apply to the removal order. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**DeinstallScheduleRequest**](DeinstallScheduleRequest.md) | Removal schedule. The requestedDateTime is mandatory. Only the STANDARD schedule type is supported for a removal.  | 
**notifications** | [**List[CrossConnectNotification]**](CrossConnectNotification.md) | Optional. The contacts are appended to the ones already held on the Cross Connect.  | [optional] 
**order** | [**OrderRequest**](OrderRequest.md) | Optional. The purchase order and the customer reference identifier replace the ones already held on the Cross Connect.  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.delete_cross_connect import DeleteCrossConnect

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCrossConnect from a JSON string
delete_cross_connect_instance = DeleteCrossConnect.from_json(json)
# print the JSON string representation of the object
print(DeleteCrossConnect.to_json())

# convert the object into a dict
delete_cross_connect_dict = delete_cross_connect_instance.to_dict()
# create an instance of DeleteCrossConnect from a dict
delete_cross_connect_from_dict = DeleteCrossConnect.from_dict(delete_cross_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


