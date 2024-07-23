# Link


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**rel** | **str** | OperationId from Swagger hub spec | [optional] 
**method** | **str** | Http method type | [optional] 
**content_type** | **str** | Content type for the response | [optional] 
**authenticate** | **bool** | Authentication required or not | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print(Link.to_json())

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_form_dict = link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


