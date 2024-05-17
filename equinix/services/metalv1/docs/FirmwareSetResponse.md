# FirmwareSetResponse

Represents single Firmware set response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**record** | [**FirmwareSet**](FirmwareSet.md) |  | [optional] 

## Example

```python
from equinix_metal.models.firmware_set_response import FirmwareSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirmwareSetResponse from a JSON string
firmware_set_response_instance = FirmwareSetResponse.from_json(json)
# print the JSON string representation of the object
print(FirmwareSetResponse.to_json())

# convert the object into a dict
firmware_set_response_dict = firmware_set_response_instance.to_dict()
# create an instance of FirmwareSetResponse from a dict
firmware_set_response_form_dict = firmware_set_response.from_dict(firmware_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


