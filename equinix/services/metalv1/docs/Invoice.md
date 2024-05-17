# Invoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**created_on** | **date** |  | [optional] 
**credit_amount** | **float** |  | [optional] 
**credits_applied** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**due_on** | **date** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | [**List[LineItem]**](LineItem.md) |  | [optional] 
**number** | **str** |  | [optional] 
**project** | [**ProjectIdName**](ProjectIdName.md) |  | [optional] 
**reference_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**target_date** | **date** |  | [optional] 

## Example

```python
from equinix_metal.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print(Invoice.to_json())

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_form_dict = invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


