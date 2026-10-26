# CrossConnectLoaRef

LOA Reference for Cross Connect. Provide either uuid or digitalLoaId. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | LOA URI. | [optional] [readonly] 
**uuid** | **str** | LOA Identifier - Attachment UUID or LOA UUID. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_loa_ref import CrossConnectLoaRef

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectLoaRef from a JSON string
cross_connect_loa_ref_instance = CrossConnectLoaRef.from_json(json)
# print the JSON string representation of the object
print(CrossConnectLoaRef.to_json())

# convert the object into a dict
cross_connect_loa_ref_dict = cross_connect_loa_ref_instance.to_dict()
# create an instance of CrossConnectLoaRef from a dict
cross_connect_loa_ref_from_dict = CrossConnectLoaRef.from_dict(cross_connect_loa_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


