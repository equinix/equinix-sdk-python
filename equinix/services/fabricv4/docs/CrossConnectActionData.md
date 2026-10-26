# CrossConnectActionData

Action Data. <br> notes and attachments are applicable for XC_INFORMATION_UPDATE and XC_DEINSTALL. <br> schedule is required for XC_DEINSTALL, where liveTrafficConsentProvided, services, notifications and order are applicable. <br> Not applicable to the other action types. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | [**List[CrossConnectActionNote]**](CrossConnectActionNote.md) | Applicable for XC_INFORMATION_UPDATE and XC_DEINSTALL. | [optional] 
**attachments** | [**List[CrossConnectAttachment]**](CrossConnectAttachment.md) | Applicable for XC_INFORMATION_UPDATE and XC_DEINSTALL. | [optional] 
**schedule** | [**DeinstallScheduleRequest**](DeinstallScheduleRequest.md) | Removal schedule. Required for XC_DEINSTALL - the requestedDateTime is mandatory and only the STANDARD schedule type is supported.  | [optional] 
**live_traffic_consent_provided** | **bool** | Applicable for XC_DEINSTALL. Confirms the customer consents to the removal even though the Cross Connect may still be carrying live traffic.  | [optional] 
**services** | [**List[CrossConnectServiceRequest]**](CrossConnectServiceRequest.md) | Applicable for XC_DEINSTALL. Only XC_PATCH_EQUIPMENT is supported for deinstall.  | [optional] 
**notifications** | [**List[CrossConnectNotification]**](CrossConnectNotification.md) | Applicable for XC_DEINSTALL. The contacts are appended to the ones already held on the Cross Connect.  | [optional] 
**order** | [**OrderRequest**](OrderRequest.md) | Applicable for XC_DEINSTALL. The purchase order and the customer reference identifier replace the ones already held on the Cross Connect.  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_data import CrossConnectActionData

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionData from a JSON string
cross_connect_action_data_instance = CrossConnectActionData.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionData.to_json())

# convert the object into a dict
cross_connect_action_data_dict = cross_connect_action_data_instance.to_dict()
# create an instance of CrossConnectActionData from a dict
cross_connect_action_data_from_dict = CrossConnectActionData.from_dict(cross_connect_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


