# LoaRequestor

Requestor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the requestor contact. | [optional] 
**org_id** | **int** | Organization ID of the requestor. | [optional] 
**org_name** | **str** | Organization name of the requestor. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_requestor import LoaRequestor

# TODO update the JSON string below
json = "{}"
# create an instance of LoaRequestor from a JSON string
loa_requestor_instance = LoaRequestor.from_json(json)
# print the JSON string representation of the object
print(LoaRequestor.to_json())

# convert the object into a dict
loa_requestor_dict = loa_requestor_instance.to_dict()
# create an instance of LoaRequestor from a dict
loa_requestor_from_dict = LoaRequestor.from_dict(loa_requestor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


