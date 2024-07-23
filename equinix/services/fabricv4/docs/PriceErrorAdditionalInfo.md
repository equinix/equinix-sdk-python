# PriceErrorAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.price_error_additional_info import PriceErrorAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PriceErrorAdditionalInfo from a JSON string
price_error_additional_info_instance = PriceErrorAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(PriceErrorAdditionalInfo.to_json())

# convert the object into a dict
price_error_additional_info_dict = price_error_additional_info_instance.to_dict()
# create an instance of PriceErrorAdditionalInfo from a dict
price_error_additional_info_form_dict = price_error_additional_info.from_dict(price_error_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


