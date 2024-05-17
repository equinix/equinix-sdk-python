# SpotMarketRequestCreateInputInstanceParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_pxe** | **bool** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**customdata** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**hostname** | **str** |  | [optional] 
**hostnames** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**locked** | **bool** | Whether the device should be locked, preventing accidental deletion. | [optional] 
**no_ssh_keys** | **bool** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**private_ipv4_subnet_size** | **int** |  | [optional] 
**project_ssh_keys** | **List[str]** |  | [optional] 
**public_ipv4_subnet_size** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**termination_time** | **datetime** |  | [optional] 
**user_ssh_keys** | **List[str]** | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] 
**userdata** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.spot_market_request_create_input_instance_parameters import SpotMarketRequestCreateInputInstanceParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SpotMarketRequestCreateInputInstanceParameters from a JSON string
spot_market_request_create_input_instance_parameters_instance = SpotMarketRequestCreateInputInstanceParameters.from_json(json)
# print the JSON string representation of the object
print(SpotMarketRequestCreateInputInstanceParameters.to_json())

# convert the object into a dict
spot_market_request_create_input_instance_parameters_dict = spot_market_request_create_input_instance_parameters_instance.to_dict()
# create an instance of SpotMarketRequestCreateInputInstanceParameters from a dict
spot_market_request_create_input_instance_parameters_form_dict = spot_market_request_create_input_instance_parameters.from_dict(spot_market_request_create_input_instance_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


