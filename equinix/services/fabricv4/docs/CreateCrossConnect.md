# CreateCrossConnect

Create Cross Connect request. A single request body supports all Cross Connect connection types - patch panel to patch panel, connection with LOA and connection to a BMMR (by Equinix or by Self). Refer to the request examples for each use case. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CrossConnectType**](CrossConnectType.md) |  | 
**name** | **str** | A short, descriptive name for this Cross Connect. | 
**bmmr_type** | [**BmmrType**](BmmrType.md) | Required when connecting to a BMMR. &lt;br&gt; Use EQUINIX when BMMR Extension is required and Equinix installs it, or SELF when you install it yourself.  | [optional] 
**circuit_id** | **str** | Circuit identifier of the Cross Connect. | [optional] 
**redundancy** | [**CrossConnectRedundancy**](CrossConnectRedundancy.md) | Provide it to place a diverse Cross Connect against an existing one - set group to the redundancy group id or the serial number of the existing Cross Connect, and priority to SECONDARY.  | [optional] 
**a_side** | [**CrossConnectASideRequest**](CrossConnectASideRequest.md) | A-Side connection details. | 
**z_side** | [**CrossConnectZSideRequest**](CrossConnectZSideRequest.md) | Z-Side connection details. &lt;br&gt; Provide the DemarcationPoint, the LOA reference or the BMMR location depending on the Cross Connect being requested.  | 
**schedule** | [**ScheduleRequest**](ScheduleRequest.md) | Preferred installation schedule. When omitted, the Cross Connect is scheduled with the STANDARD schedule code.  | [optional] 
**services** | [**List[CrossConnectServiceRequest]**](CrossConnectServiceRequest.md) | Cross Connect Services. | [optional] 
**notifications** | [**List[CrossConnectNotification]**](CrossConnectNotification.md) | Preferences for notifications on Cross Connect configuration or status changes.  | [optional] 
**order** | [**OrderRequest**](OrderRequest.md) |  | [optional] 
**notes** | [**List[CrossConnectNoteRequest]**](CrossConnectNoteRequest.md) | Additional Note. | [optional] 
**attachments** | [**List[CrossConnectAttachment]**](CrossConnectAttachment.md) | Additional Attachments. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.create_cross_connect import CreateCrossConnect

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCrossConnect from a JSON string
create_cross_connect_instance = CreateCrossConnect.from_json(json)
# print the JSON string representation of the object
print(CreateCrossConnect.to_json())

# convert the object into a dict
create_cross_connect_dict = create_cross_connect_instance.to_dict()
# create an instance of CreateCrossConnect from a dict
create_cross_connect_from_dict = CreateCrossConnect.from_dict(create_cross_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


