# IpBlockLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metro_href** | **str** | Metro URL path for the linked resource | [optional] 
**metro_code** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_location import IpBlockLocation

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockLocation from a JSON string
ip_block_location_instance = IpBlockLocation.from_json(json)
# print the JSON string representation of the object
print(IpBlockLocation.to_json())

# convert the object into a dict
ip_block_location_dict = ip_block_location_instance.to_dict()
# create an instance of IpBlockLocation from a dict
ip_block_location_from_dict = IpBlockLocation.from_dict(ip_block_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


