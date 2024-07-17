# PriceLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metro_code** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.price_location import PriceLocation

# TODO update the JSON string below
json = "{}"
# create an instance of PriceLocation from a JSON string
price_location_instance = PriceLocation.from_json(json)
# print the JSON string representation of the object
print(PriceLocation.to_json())

# convert the object into a dict
price_location_dict = price_location_instance.to_dict()
# create an instance of PriceLocation from a dict
price_location_form_dict = price_location.from_dict(price_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


