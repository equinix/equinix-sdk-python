# Invitation1


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
from equinix.services.metalv1.models.invitation1 import Invitation1

# TODO update the JSON string below
json = "{}"
# create an instance of Invitation1 from a JSON string
invitation1_instance = Invitation1.from_json(json)
# print the JSON string representation of the object
print(Invitation1.to_json())

# convert the object into a dict
invitation1_dict = invitation1_instance.to_dict()
# create an instance of Invitation1 from a dict
invitation1_from_dict = Invitation1.from_dict(invitation1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


