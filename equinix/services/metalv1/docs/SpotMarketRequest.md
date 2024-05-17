# SpotMarketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**devices_max** | **int** |  | [optional] 
**devices_min** | **int** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**facilities** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instances** | [**Href**](Href.md) |  | [optional] 
**max_bid_price** | **float** |  | [optional] 
**metro** | [**SpotMarketRequestMetro**](SpotMarketRequestMetro.md) |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_request import SpotMarketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketRequest from a JSON string
spot_market_request_instance = SpotMarketRequest.from_json(json)
# print the JSON string representation of the object
print(SpotMarketRequest.to_json())

# convert the object into a dict
spot_market_request_dict = spot_market_request_instance.to_dict()
# create an instance of SpotMarketRequest from a dict
spot_market_request_form_dict = spot_market_request.from_dict(spot_market_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


