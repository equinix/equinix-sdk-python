# SpotMarketRequestMetro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_request_metro import SpotMarketRequestMetro

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketRequestMetro from a JSON string
spot_market_request_metro_instance = SpotMarketRequestMetro.from_json(json)
# print the JSON string representation of the object
print(SpotMarketRequestMetro.to_json())

# convert the object into a dict
spot_market_request_metro_dict = spot_market_request_metro_instance.to_dict()
# create an instance of SpotMarketRequestMetro from a dict
spot_market_request_metro_form_dict = spot_market_request_metro.from_dict(spot_market_request_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


