# IssueLoa

Issue Loa

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LoaType**](LoaType.md) |  | 
**name** | **str** | A short, descriptive name for this LOA. | 
**description** | **str** | Additional context about this LOA. | [optional] 
**authorized_product_type** | [**LoaProductType**](LoaProductType.md) |  | 
**expiration_date_time** | **datetime** | Date and time when this LOA expires.&lt;br&gt; Default to 3 months from the creation date  | [optional] 
**requestor** | [**LoaRequestor**](LoaRequestor.md) |  | [optional] 
**demarcation_point** | [**LoaDemarcationPoint**](LoaDemarcationPoint.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.issue_loa import IssueLoa

# TODO update the JSON string below
json = "{}"
# create an instance of IssueLoa from a JSON string
issue_loa_instance = IssueLoa.from_json(json)
# print the JSON string representation of the object
print(IssueLoa.to_json())

# convert the object into a dict
issue_loa_dict = issue_loa_instance.to_dict()
# create an instance of IssueLoa from a dict
issue_loa_from_dict = IssueLoa.from_dict(issue_loa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


