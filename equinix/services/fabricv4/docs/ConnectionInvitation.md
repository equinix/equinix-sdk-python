# ConnectionInvitation

Connection Invitation Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | invitee email | [optional] 
**message** | **str** | invitation message | [optional] 
**ctr_draft_order_id** | **str** | draft order id for invitation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_invitation import ConnectionInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionInvitation from a JSON string
connection_invitation_instance = ConnectionInvitation.from_json(json)
# print the JSON string representation of the object
print(ConnectionInvitation.to_json())

# convert the object into a dict
connection_invitation_dict = connection_invitation_instance.to_dict()
# create an instance of ConnectionInvitation from a dict
connection_invitation_form_dict = connection_invitation.from_dict(connection_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


