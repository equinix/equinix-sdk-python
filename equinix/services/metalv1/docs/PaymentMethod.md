# PaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**PaymentMethodBillingAddress**](PaymentMethodBillingAddress.md) |  | [optional] 
**card_type** | **str** |  | [optional] 
**cardholder_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by_user** | [**Href**](Href.md) |  | [optional] 
**default** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**expiration_month** | **str** |  | [optional] 
**expiration_year** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**projects** | [**List[Href]**](Href.md) |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print(PaymentMethod.to_json())

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_form_dict = payment_method.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


