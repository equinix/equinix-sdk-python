# Entitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**feature_access** | **object** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | 
**instance_quota** | **object** |  | [optional] 
**ip_quota** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**project_quota** | **int** |  | [optional] [default to 0]
**slug** | **str** |  | 
**volume_limits** | **object** |  | [optional] 
**volume_quota** | **object** |  | [optional] 
**weight** | **int** |  | 

## Example

```python
from equinix_metal.models.entitlement import Entitlement

# TODO update the JSON string below
json = "{}"
# create an instance of Entitlement from a JSON string
entitlement_instance = Entitlement.from_json(json)
# print the JSON string representation of the object
print(Entitlement.to_json())

# convert the object into a dict
entitlement_dict = entitlement_instance.to_dict()
# create an instance of Entitlement from a dict
entitlement_form_dict = entitlement.from_dict(entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


