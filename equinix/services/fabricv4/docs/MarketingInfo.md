# MarketingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** | Logo file name | [optional] 
**promotion** | **bool** | Profile promotion on marketplace | [optional] 
**process_steps** | [**List[ProcessStep]**](ProcessStep.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.marketing_info import MarketingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingInfo from a JSON string
marketing_info_instance = MarketingInfo.from_json(json)
# print the JSON string representation of the object
print(MarketingInfo.to_json())

# convert the object into a dict
marketing_info_dict = marketing_info_instance.to_dict()
# create an instance of MarketingInfo from a dict
marketing_info_form_dict = marketing_info.from_dict(marketing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


