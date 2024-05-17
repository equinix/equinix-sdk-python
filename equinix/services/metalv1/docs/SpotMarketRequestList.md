# SpotMarketRequestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**spot_market_requests** | [**List[SpotMarketRequest]**](SpotMarketRequest.md) |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_request_list import SpotMarketRequestList

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketRequestList from a JSON string
spot_market_request_list_instance = SpotMarketRequestList.from_json(json)
# print the JSON string representation of the object
print(SpotMarketRequestList.to_json())

# convert the object into a dict
spot_market_request_list_dict = spot_market_request_list_instance.to_dict()
# create an instance of SpotMarketRequestList from a dict
spot_market_request_list_form_dict = spot_market_request_list.from_dict(spot_market_request_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


