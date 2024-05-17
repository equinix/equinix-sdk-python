# PaymentMethodCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | 
**nonce** | **str** |  | 

## Example

```python
from equinix_metal.models.payment_method_create_input import PaymentMethodCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCreateInput from a JSON string
payment_method_create_input_instance = PaymentMethodCreateInput.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCreateInput.to_json())

# convert the object into a dict
payment_method_create_input_dict = payment_method_create_input_instance.to_dict()
# create an instance of PaymentMethodCreateInput from a dict
payment_method_create_input_form_dict = payment_method_create_input.from_dict(payment_method_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


