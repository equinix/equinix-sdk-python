# TagRequest

Equinix Fabric Tag Request Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of tag | 
**name** | **str** | Name of the Tag | 
**display_name** | **str** | Display name of the Tag | 

## Example

```python
from equinix.services.fabricv4.models.tag_request import TagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagRequest from a JSON string
tag_request_instance = TagRequest.from_json(json)
# print the JSON string representation of the object
print(TagRequest.to_json())

# convert the object into a dict
tag_request_dict = tag_request_instance.to_dict()
# create an instance of TagRequest from a dict
tag_request_from_dict = TagRequest.from_dict(tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


