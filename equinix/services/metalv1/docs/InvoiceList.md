# InvoiceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**invoices** | [**List[Invoice]**](Invoice.md) |  | [optional] 

## Example

```python
from equinix_metal.models.invoice_list import InvoiceList

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceList from a JSON string
invoice_list_instance = InvoiceList.from_json(json)
# print the JSON string representation of the object
print(InvoiceList.to_json())

# convert the object into a dict
invoice_list_dict = invoice_list_instance.to_dict()
# create an instance of InvoiceList from a dict
invoice_list_form_dict = invoice_list.from_dict(invoice_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


