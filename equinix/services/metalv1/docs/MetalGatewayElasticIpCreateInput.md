# MetalGatewayElasticIpCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An IP address (or IP Address range) contained within one of the project&#39;s IP Reservations | 
**customdata** | **Dict[str, object]** | Optional User-defined JSON object value. | [optional] 
**href** | **str** |  | [optional] 
**next_hop** | **str** | An IP address contained within the Metal Gateways&#39; IP Reservation range. | 
**tags** | **List[str]** | Optional list of User-defined tags. Can be used by users to provide additional details or context regarding the purpose or usage of this resource. | [optional] 

## Example

```python
from equinix_metal.models.metal_gateway_elastic_ip_create_input import MetalGatewayElasticIpCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetalGatewayElasticIpCreateInput from a JSON string
metal_gateway_elastic_ip_create_input_instance = MetalGatewayElasticIpCreateInput.from_json(json)
# print the JSON string representation of the object
print(MetalGatewayElasticIpCreateInput.to_json())

# convert the object into a dict
metal_gateway_elastic_ip_create_input_dict = metal_gateway_elastic_ip_create_input_instance.to_dict()
# create an instance of MetalGatewayElasticIpCreateInput from a dict
metal_gateway_elastic_ip_create_input_form_dict = metal_gateway_elastic_ip_create_input.from_dict(metal_gateway_elastic_ip_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


