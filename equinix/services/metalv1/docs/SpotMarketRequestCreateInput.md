# SpotMarketRequestCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices_max** | **int** |  | [optional] 
**devices_min** | **int** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**facilities** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**instance_parameters** | [**SpotMarketRequestCreateInputInstanceParameters**](SpotMarketRequestCreateInputInstanceParameters.md) |  | [optional] 
**max_bid_price** | **float** |  | [optional] 
**metro** | **str** | The metro ID or code the spot market request will be created in. | [optional] 

## Example

```python
from equinix_metal.models.spot_market_request_create_input import SpotMarketRequestCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketRequestCreateInput from a JSON string
spot_market_request_create_input_instance = SpotMarketRequestCreateInput.from_json(json)
# print the JSON string representation of the object
print(SpotMarketRequestCreateInput.to_json())

# convert the object into a dict
spot_market_request_create_input_dict = spot_market_request_create_input_instance.to_dict()
# create an instance of SpotMarketRequestCreateInput from a dict
spot_market_request_create_input_form_dict = spot_market_request_create_input.from_dict(spot_market_request_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


