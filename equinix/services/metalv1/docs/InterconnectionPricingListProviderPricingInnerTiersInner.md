# InterconnectionPricingListProviderPricingInnerTiersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | **int** | Bandwidth tier in Mbps | [optional] 
**billing_cycle** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_pricing_list_provider_pricing_inner_tiers_inner import InterconnectionPricingListProviderPricingInnerTiersInner

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionPricingListProviderPricingInnerTiersInner from a JSON string
interconnection_pricing_list_provider_pricing_inner_tiers_inner_instance = InterconnectionPricingListProviderPricingInnerTiersInner.from_json(json)
# print the JSON string representation of the object
print(InterconnectionPricingListProviderPricingInnerTiersInner.to_json())

# convert the object into a dict
interconnection_pricing_list_provider_pricing_inner_tiers_inner_dict = interconnection_pricing_list_provider_pricing_inner_tiers_inner_instance.to_dict()
# create an instance of InterconnectionPricingListProviderPricingInnerTiersInner from a dict
interconnection_pricing_list_provider_pricing_inner_tiers_inner_form_dict = interconnection_pricing_list_provider_pricing_inner_tiers_inner.from_dict(interconnection_pricing_list_provider_pricing_inner_tiers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


