# CrossConnectActionResponseData

Action Data. <br> notes and attachments are applicable for XC_INFORMATION_UPDATE and XC_DEINSTALL. <br> schedule, services, liveTrafficConsentProvided, notifications and order are applicable for XC_DEINSTALL. <br> Each schedule, service, note and attachment carries the href and the uuid of the sub-resource it refers to. <br> Not applicable to the other action types. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**List[CrossConnectActionNoteResponse]**](CrossConnectActionNoteResponse.md) | Applicable for XC_INFORMATION_UPDATE and XC_DEINSTALL. | [optional] [readonly] 
**attachments** | [**List[CrossConnectActionAttachmentResponse]**](CrossConnectActionAttachmentResponse.md) | Applicable for XC_INFORMATION_UPDATE and XC_DEINSTALL. | [optional] [readonly] 
**schedule** | [**CrossConnectScheduleResponse**](CrossConnectScheduleResponse.md) | Applicable for XC_DEINSTALL. | [optional] [readonly] 
**live_traffic_consent_provided** | **bool** | Applicable for XC_DEINSTALL. Confirms the customer consents to the removal even though the Cross Connect may still be carrying live traffic.  | [optional] [readonly] 
**services** | [**List[CrossConnectServiceResponse]**](CrossConnectServiceResponse.md) | Applicable for XC_DEINSTALL. Only XC_PATCH_EQUIPMENT is supported for deinstall.  | [optional] [readonly] 
**notifications** | [**List[CrossConnectNotification]**](CrossConnectNotification.md) | Applicable for XC_DEINSTALL. The contacts are appended to the ones already held on the Cross Connect.  | [optional] [readonly] 
**order** | [**OrderResponse**](OrderResponse.md) | Applicable for XC_DEINSTALL. The purchase order and the customer reference identifier replace the ones already held on the Cross Connect.  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_response_data import CrossConnectActionResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionResponseData from a JSON string
cross_connect_action_response_data_instance = CrossConnectActionResponseData.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionResponseData.to_json())

# convert the object into a dict
cross_connect_action_response_data_dict = cross_connect_action_response_data_instance.to_dict()
# create an instance of CrossConnectActionResponseData from a dict
cross_connect_action_response_data_from_dict = CrossConnectActionResponseData.from_dict(cross_connect_action_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


