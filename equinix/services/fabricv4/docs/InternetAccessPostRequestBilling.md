# InternetAccessPostRequestBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InternetAccessBillingType**](InternetAccessBillingType.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_post_request_billing import InternetAccessPostRequestBilling

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessPostRequestBilling from a JSON string
internet_access_post_request_billing_instance = InternetAccessPostRequestBilling.from_json(json)
# print the JSON string representation of the object
print(InternetAccessPostRequestBilling.to_json())

# convert the object into a dict
internet_access_post_request_billing_dict = internet_access_post_request_billing_instance.to_dict()
# create an instance of InternetAccessPostRequestBilling from a dict
internet_access_post_request_billing_from_dict = InternetAccessPostRequestBilling.from_dict(internet_access_post_request_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


