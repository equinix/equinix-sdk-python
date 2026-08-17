# LoaActionData

Action Data. <br> For LOA_ISSUER_AUTHORIZATION — always required. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**demarcation_point** | [**LoaDemarcationPoint**](LoaDemarcationPoint.md) |  | [optional] 
**expiration_date_time** | **datetime** | Date and time when this LOA expires.&lt;br&gt; Default to 3 months from the creation date  | [optional] 
**portal_url** | **str** | Portal URL for the LOA to either accept from requestor &lt;br&gt; or authorize from the issuer.  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_data import LoaActionData

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionData from a JSON string
loa_action_data_instance = LoaActionData.from_json(json)
# print the JSON string representation of the object
print(LoaActionData.to_json())

# convert the object into a dict
loa_action_data_dict = loa_action_data_instance.to_dict()
# create an instance of LoaActionData from a dict
loa_action_data_from_dict = LoaActionData.from_dict(loa_action_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


