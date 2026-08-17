# LoaResponse

Loa Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of this LOA resource. | [optional] 
**uuid** | **str** | Unique identifier of this LOA. | [optional] 
**type** | [**LoaType**](LoaType.md) |  | [optional] 
**name** | **str** | A short, descriptive name for this LOA | [optional] 
**description** | **str** | Additional context about this LOA | [optional] 
**authorized_product_type** | [**LoaProductType**](LoaProductType.md) |  | [optional] 
**state** | [**LoaState**](LoaState.md) |  | [optional] 
**operation** | [**LoaResponseOperation**](LoaResponseOperation.md) |  | [optional] 
**requestor** | [**LoaRequestor**](LoaRequestor.md) |  | [optional] 
**issuer** | [**LoaIssuer**](LoaIssuer.md) |  | [optional] 
**demarcation_point** | [**LoaDemarcationPoint**](LoaDemarcationPoint.md) |  | [optional] 
**location** | [**LoaLocation**](LoaLocation.md) |  | [optional] 
**expiration_date_time** | **datetime** | Date and time when this LOA expires.&lt;br&gt; Default to 3 months from the creation date  | [optional] 
**change_log** | [**LoaChangelog**](LoaChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_response import LoaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoaResponse from a JSON string
loa_response_instance = LoaResponse.from_json(json)
# print the JSON string representation of the object
print(LoaResponse.to_json())

# convert the object into a dict
loa_response_dict = loa_response_instance.to_dict()
# create an instance of LoaResponse from a dict
loa_response_from_dict = LoaResponse.from_dict(loa_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


