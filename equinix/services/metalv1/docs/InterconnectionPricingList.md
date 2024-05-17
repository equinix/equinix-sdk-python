# InterconnectionPricingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**provider_pricing** | [**List[InterconnectionPricingListProviderPricingInner]**](InterconnectionPricingListProviderPricingInner.md) | Pricing information per connection provider. | [optional] 

## Example

```python
from equinix_metal.models.interconnection_pricing_list import InterconnectionPricingList

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionPricingList from a JSON string
interconnection_pricing_list_instance = InterconnectionPricingList.from_json(json)
# print the JSON string representation of the object
print(InterconnectionPricingList.to_json())

# convert the object into a dict
interconnection_pricing_list_dict = interconnection_pricing_list_instance.to_dict()
# create an instance of InterconnectionPricingList from a dict
interconnection_pricing_list_form_dict = interconnection_pricing_list.from_dict(interconnection_pricing_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


