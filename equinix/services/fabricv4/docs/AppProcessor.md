# AppProcessor

App Processor object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppProcessorType**](AppProcessorType.md) |  | [default to AppProcessorType.APP_PROCESSOR]
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Customer-provided App Processor name | 
**description** | **str** | Customer-provided App Processor description | [optional] 
**state** | [**AppProcessorState**](AppProcessorState.md) |  | [optional] 
**registry_id** | **str** | Container image reference for the processor runtime | 
**marketplace** | [**AppProcessorMarketplace**](AppProcessorMarketplace.md) |  | 
**project** | [**Project**](Project.md) |  | 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**AppProcessorChange**](AppProcessorChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_processor import AppProcessor

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessor from a JSON string
app_processor_instance = AppProcessor.from_json(json)
# print the JSON string representation of the object
print(AppProcessor.to_json())

# convert the object into a dict
app_processor_dict = app_processor_instance.to_dict()
# create an instance of AppProcessor from a dict
app_processor_from_dict = AppProcessor.from_dict(app_processor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


