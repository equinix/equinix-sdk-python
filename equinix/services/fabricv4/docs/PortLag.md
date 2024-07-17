# PortLag

Port Lag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id | [optional] 
**enabled** | **bool** | enabled | [optional] 
**name** | **str** | name | [optional] 
**member_status** | **str** | member status | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_lag import PortLag

# TODO update the JSON string below
json = "{}"
# create an instance of PortLag from a JSON string
port_lag_instance = PortLag.from_json(json)
# print the JSON string representation of the object
print(PortLag.to_json())

# convert the object into a dict
port_lag_dict = port_lag_instance.to_dict()
# create an instance of PortLag from a dict
port_lag_form_dict = port_lag.from_dict(port_lag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


