# InterconnectionPricingListProviderPricingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**tiers** | [**List[InterconnectionPricingListProviderPricingInnerTiersInner]**](InterconnectionPricingListProviderPricingInnerTiersInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_pricing_list_provider_pricing_inner import InterconnectionPricingListProviderPricingInner

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionPricingListProviderPricingInner from a JSON string
interconnection_pricing_list_provider_pricing_inner_instance = InterconnectionPricingListProviderPricingInner.from_json(json)
# print the JSON string representation of the object
print(InterconnectionPricingListProviderPricingInner.to_json())

# convert the object into a dict
interconnection_pricing_list_provider_pricing_inner_dict = interconnection_pricing_list_provider_pricing_inner_instance.to_dict()
# create an instance of InterconnectionPricingListProviderPricingInner from a dict
interconnection_pricing_list_provider_pricing_inner_form_dict = interconnection_pricing_list_provider_pricing_inner.from_dict(interconnection_pricing_list_provider_pricing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


