# InternetAccessOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_order_number** | **str** | Purchase order number | [optional] 
**customer_reference_number** | **str** | Customer reference number | [optional] 
**billing_tier** | **str** | Billing tier for connection bandwidth | [optional] 
**order_id** | **str** | Order Identification | [optional] 
**order_number** | **str** | Order Reference Number | [optional] 
**term_length** | **int** | Term length in months, valid values are 1, 12, 24, 36 where 1 is the default value (for on-demand case). | [optional] [default to 1]
**contracted_bandwidth** | **int** | Contracted bandwidth | [optional] 
**href** | **str** | Order URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_order import InternetAccessOrder

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessOrder from a JSON string
internet_access_order_instance = InternetAccessOrder.from_json(json)
# print the JSON string representation of the object
print(InternetAccessOrder.to_json())

# convert the object into a dict
internet_access_order_dict = internet_access_order_instance.to_dict()
# create an instance of InternetAccessOrder from a dict
internet_access_order_from_dict = InternetAccessOrder.from_dict(internet_access_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


