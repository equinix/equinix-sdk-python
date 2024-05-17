# PaymentMethodUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | **object** |  | [optional] 
**cardholder_name** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 
**expiration_month** | **str** |  | [optional] 
**expiration_year** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.payment_method_update_input import PaymentMethodUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodUpdateInput from a JSON string
payment_method_update_input_instance = PaymentMethodUpdateInput.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodUpdateInput.to_json())

# convert the object into a dict
payment_method_update_input_dict = payment_method_update_input_instance.to_dict()
# create an instance of PaymentMethodUpdateInput from a dict
payment_method_update_input_form_dict = payment_method_update_input.from_dict(payment_method_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


