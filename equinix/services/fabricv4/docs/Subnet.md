# Subnet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SubnetType**](SubnetType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**vpc_id** | **str** |  | [optional] 
**ipv4** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.subnet import Subnet

# TODO update the JSON string below
json = "{}"
# create an instance of Subnet from a JSON string
subnet_instance = Subnet.from_json(json)
# print the JSON string representation of the object
print(Subnet.to_json())

# convert the object into a dict
subnet_dict = subnet_instance.to_dict()
# create an instance of Subnet from a dict
subnet_from_dict = Subnet.from_dict(subnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


