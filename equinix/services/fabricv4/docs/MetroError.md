# MetroError

Error with details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | [**MetroErrorErrorCode**](MetroErrorErrorCode.md) |  | 
**error_message** | [**MetroErrorErrorMessage**](MetroErrorErrorMessage.md) |  | 
**correlation_id** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**help** | **str** |  | [optional] 
**additional_info** | [**List[PriceErrorAdditionalInfo]**](PriceErrorAdditionalInfo.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metro_error import MetroError

# TODO update the JSON string below
json = "{}"
# create an instance of MetroError from a JSON string
metro_error_instance = MetroError.from_json(json)
# print the JSON string representation of the object
print(MetroError.to_json())

# convert the object into a dict
metro_error_dict = metro_error_instance.to_dict()
# create an instance of MetroError from a dict
metro_error_form_dict = metro_error.from_dict(metro_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


