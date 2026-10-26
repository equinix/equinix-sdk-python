# PatchEquipmentRequest

Patch equipment installed for the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cabinet_unique_space_id** | **str** | Unique identifier of the Cabinet. | 
**port** | **int** | Port number. | 
**connector_type** | **str** | Connector Type. | 

## Example

```python
from equinix.services.fabricv4.models.patch_equipment_request import PatchEquipmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchEquipmentRequest from a JSON string
patch_equipment_request_instance = PatchEquipmentRequest.from_json(json)
# print the JSON string representation of the object
print(PatchEquipmentRequest.to_json())

# convert the object into a dict
patch_equipment_request_dict = patch_equipment_request_instance.to_dict()
# create an instance of PatchEquipmentRequest from a dict
patch_equipment_request_from_dict = PatchEquipmentRequest.from_dict(patch_equipment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


