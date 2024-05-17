# PaymentMethodBillingAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code_alpha2** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.payment_method_billing_address import PaymentMethodBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBillingAddress from a JSON string
payment_method_billing_address_instance = PaymentMethodBillingAddress.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBillingAddress.to_json())

# convert the object into a dict
payment_method_billing_address_dict = payment_method_billing_address_instance.to_dict()
# create an instance of PaymentMethodBillingAddress from a dict
payment_method_billing_address_form_dict = payment_method_billing_address.from_dict(payment_method_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


