# ServiceMetro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | metro code | [optional] 
**name** | **str** | metro name | [optional] 
**vc_bandwidth_max** | **int** | max VC speed supported in Mbps | [optional] 
**ibxs** | **List[str]** |  | [optional] 
**in_trail** | **bool** |  | [optional] 
**display_name** | **str** | service metro display name | [optional] 
**seller_regions** | **Dict[str, str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_metro import ServiceMetro

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMetro from a JSON string
service_metro_instance = ServiceMetro.from_json(json)
# print the JSON string representation of the object
print(ServiceMetro.to_json())

# convert the object into a dict
service_metro_dict = service_metro_instance.to_dict()
# create an instance of ServiceMetro from a dict
service_metro_from_dict = ServiceMetro.from_dict(service_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


