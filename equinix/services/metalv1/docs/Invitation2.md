# Invitation2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invitation** | [**Href**](Href.md) |  | [optional] 
**invited_by** | [**Href**](Href.md) |  | [optional] 
**invitee** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**projects** | [**List[Href]**](Href.md) |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix.services.metalv1.models.invitation2 import Invitation2

# TODO update the JSON string below
json = "{}"
# create an instance of Invitation2 from a JSON string
invitation2_instance = Invitation2.from_json(json)
# print the JSON string representation of the object
print(Invitation2.to_json())

# convert the object into a dict
invitation2_dict = invitation2_instance.to_dict()
# create an instance of Invitation2 from a dict
invitation2_from_dict = Invitation2.from_dict(invitation2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


