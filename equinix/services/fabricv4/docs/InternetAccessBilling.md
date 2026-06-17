# InternetAccessBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InternetAccessBillingType**](InternetAccessBillingType.md) |  | 
**enabled** | **bool** | Indicates whether the billing is enabled | [optional] 
**start_date** | **datetime** | The start date for the billing period | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_billing import InternetAccessBilling

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessBilling from a JSON string
internet_access_billing_instance = InternetAccessBilling.from_json(json)
# print the JSON string representation of the object
print(InternetAccessBilling.to_json())

# convert the object into a dict
internet_access_billing_dict = internet_access_billing_instance.to_dict()
# create an instance of InternetAccessBilling from a dict
internet_access_billing_from_dict = InternetAccessBilling.from_dict(internet_access_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


