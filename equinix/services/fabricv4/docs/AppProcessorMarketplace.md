# AppProcessorMarketplace

App Processor marketplace settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**AppProcessorMarketplaceVisibility**](AppProcessorMarketplaceVisibility.md) |  | [default to AppProcessorMarketplaceVisibility.PUBLIC]

## Example

```python
from equinix.services.fabricv4.models.app_processor_marketplace import AppProcessorMarketplace

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorMarketplace from a JSON string
app_processor_marketplace_instance = AppProcessorMarketplace.from_json(json)
# print the JSON string representation of the object
print(AppProcessorMarketplace.to_json())

# convert the object into a dict
app_processor_marketplace_dict = app_processor_marketplace_instance.to_dict()
# create an instance of AppProcessorMarketplace from a dict
app_processor_marketplace_from_dict = AppProcessorMarketplace.from_dict(app_processor_marketplace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


