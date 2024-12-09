# EndCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_disclosed** | **bool** | Indicate if endCustomer info should be disclosed or not | [optional] [default to False]
**name** | **str** |  | [optional] 
**mdm_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.end_customer import EndCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of EndCustomer from a JSON string
end_customer_instance = EndCustomer.from_json(json)
# print the JSON string representation of the object
print(EndCustomer.to_json())

# convert the object into a dict
end_customer_dict = end_customer_instance.to_dict()
# create an instance of EndCustomer from a dict
end_customer_form_dict = end_customer.from_dict(end_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


