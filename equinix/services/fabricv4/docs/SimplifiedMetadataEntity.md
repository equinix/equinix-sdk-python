# SimplifiedMetadataEntity

Configuration details for port used at the access point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | url to entity | [optional] 
**uuid** | **str** | Equinix assigned Identifier | [optional] 
**type** | **str** | Type of Port | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_metadata_entity import SimplifiedMetadataEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedMetadataEntity from a JSON string
simplified_metadata_entity_instance = SimplifiedMetadataEntity.from_json(json)
# print the JSON string representation of the object
print(SimplifiedMetadataEntity.to_json())

# convert the object into a dict
simplified_metadata_entity_dict = simplified_metadata_entity_instance.to_dict()
# create an instance of SimplifiedMetadataEntity from a dict
simplified_metadata_entity_form_dict = simplified_metadata_entity.from_dict(simplified_metadata_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


