# LastMileConfig

Last mile configuration for the connection. Applicable to zSide only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** | Last mile service type | [optional] 
**bandwidth** | **int** | Last mile bandwidth in Mbps | [optional] 
**address** | **str** | Last mile address | [optional] 
**notifications** | [**List[LastMileNotificationInfo]**](LastMileNotificationInfo.md) | Last mile notification contacts | [optional] 

## Example

```python
from equinix.services.fabricv4.models.last_mile_config import LastMileConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LastMileConfig from a JSON string
last_mile_config_instance = LastMileConfig.from_json(json)
# print the JSON string representation of the object
print(LastMileConfig.to_json())

# convert the object into a dict
last_mile_config_dict = last_mile_config_instance.to_dict()
# create an instance of LastMileConfig from a dict
last_mile_config_from_dict = LastMileConfig.from_dict(last_mile_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


