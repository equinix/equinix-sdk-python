# OpticalConnectBulk

Dual diverse pair Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpticalConnectResponse]**](OpticalConnectResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_bulk import OpticalConnectBulk

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectBulk from a JSON string
optical_connect_bulk_instance = OpticalConnectBulk.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectBulk.to_json())

# convert the object into a dict
optical_connect_bulk_dict = optical_connect_bulk_instance.to_dict()
# create an instance of OpticalConnectBulk from a dict
optical_connect_bulk_from_dict = OpticalConnectBulk.from_dict(optical_connect_bulk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


