# InternetAccessOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number | [optional] 
**order_number** | **str** | Order Number | [optional] 
**order_line** | **str** | Order Line Number | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_order_request import InternetAccessOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessOrderRequest from a JSON string
internet_access_order_request_instance = InternetAccessOrderRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessOrderRequest.to_json())

# convert the object into a dict
internet_access_order_request_dict = internet_access_order_request_instance.to_dict()
# create an instance of InternetAccessOrderRequest from a dict
internet_access_order_request_from_dict = InternetAccessOrderRequest.from_dict(internet_access_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


