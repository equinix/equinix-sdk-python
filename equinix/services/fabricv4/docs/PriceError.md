# PriceError

Error with details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | [**PriceErrorErrorCode**](PriceErrorErrorCode.md) |  | 
**error_message** | [**PriceErrorErrorMessage**](PriceErrorErrorMessage.md) |  | 
**correlation_id** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**help** | **str** |  | [optional] 
**additional_info** | [**List[PriceErrorAdditionalInfo]**](PriceErrorAdditionalInfo.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.price_error import PriceError

# TODO update the JSON string below
json = "{}"
# create an instance of PriceError from a JSON string
price_error_instance = PriceError.from_json(json)
# print the JSON string representation of the object
print(PriceError.to_json())

# convert the object into a dict
price_error_dict = price_error_instance.to_dict()
# create an instance of PriceError from a dict
price_error_from_dict = PriceError.from_dict(price_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


