# InterconnectLocation

Interconnect metro location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Metro URI | [optional] 
**metro_code** | **str** | Metro code where the interconnect is created | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_location import InterconnectLocation

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectLocation from a JSON string
interconnect_location_instance = InterconnectLocation.from_json(json)
# print the JSON string representation of the object
print(InterconnectLocation.to_json())

# convert the object into a dict
interconnect_location_dict = interconnect_location_instance.to_dict()
# create an instance of InterconnectLocation from a dict
interconnect_location_from_dict = InterconnectLocation.from_dict(interconnect_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


