# PatchEquipmentResponse

Patch equipment installed for the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cabinet_unique_space_id** | **str** | Unique identifier of the Cabinet. | [optional] 
**port** | **int** | Port number. | [optional] 
**connector_type** | **str** | Connector Type. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.patch_equipment_response import PatchEquipmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PatchEquipmentResponse from a JSON string
patch_equipment_response_instance = PatchEquipmentResponse.from_json(json)
# print the JSON string representation of the object
print(PatchEquipmentResponse.to_json())

# convert the object into a dict
patch_equipment_response_dict = patch_equipment_response_instance.to_dict()
# create an instance of PatchEquipmentResponse from a dict
patch_equipment_response_from_dict = PatchEquipmentResponse.from_dict(patch_equipment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


