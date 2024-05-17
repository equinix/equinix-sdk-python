# FirmwareSetListResponse

Represents collection of Firmware Sets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**page** | **int** | Page returned | [optional] 
**page_count** | **int** | Items returned in current page | [optional] 
**page_size** | **int** | Max number of items returned in a page | [optional] 
**records** | [**List[FirmwareSet]**](FirmwareSet.md) | Represents a list of FirmwareSets | [optional] 
**total_pages** | **int** | Total count of pages | [optional] 
**total_record_count** | **int** | Total count of items | [optional] 

## Example

```python
from equinix_metal.models.firmware_set_list_response import FirmwareSetListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirmwareSetListResponse from a JSON string
firmware_set_list_response_instance = FirmwareSetListResponse.from_json(json)
# print the JSON string representation of the object
print(FirmwareSetListResponse.to_json())

# convert the object into a dict
firmware_set_list_response_dict = firmware_set_list_response_instance.to_dict()
# create an instance of FirmwareSetListResponse from a dict
firmware_set_list_response_form_dict = firmware_set_list_response.from_dict(firmware_set_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


