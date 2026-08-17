# InterconnectLocationRequest

Interconnect location for create request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metro_code** | **str** | Metro code where the interconnect is created | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_location_request import InterconnectLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectLocationRequest from a JSON string
interconnect_location_request_instance = InterconnectLocationRequest.from_json(json)
# print the JSON string representation of the object
print(InterconnectLocationRequest.to_json())

# convert the object into a dict
interconnect_location_request_dict = interconnect_location_request_instance.to_dict()
# create an instance of InterconnectLocationRequest from a dict
interconnect_location_request_from_dict = InterconnectLocationRequest.from_dict(interconnect_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


