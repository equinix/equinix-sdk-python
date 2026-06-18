# SubmitIpBlockRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**IpBlockLocation**](IpBlockLocation.md) |  | [optional] 
**type** | [**TypeOfIpBlockProduct**](TypeOfIpBlockProduct.md) |  | 
**project** | [**IpBlockProjectRequest**](IpBlockProjectRequest.md) |  | 
**account** | [**IpBlockAccount**](IpBlockAccount.md) |  | [optional] 
**order** | [**IpBlockOrderRequest**](IpBlockOrderRequest.md) |  | [optional] 
**regulations** | [**IpBlockRegulations**](IpBlockRegulations.md) |  | [optional] 
**prefix_length** | **int** | IpBlockPrefix length | [optional] 
**prefix** | **str** | CIDR prefix | [optional] 

## Example

```python
from equinix.services.fabricv4.models.submit_ip_block_request_body import SubmitIpBlockRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitIpBlockRequestBody from a JSON string
submit_ip_block_request_body_instance = SubmitIpBlockRequestBody.from_json(json)
# print the JSON string representation of the object
print(SubmitIpBlockRequestBody.to_json())

# convert the object into a dict
submit_ip_block_request_body_dict = submit_ip_block_request_body_instance.to_dict()
# create an instance of SubmitIpBlockRequestBody from a dict
submit_ip_block_request_body_from_dict = SubmitIpBlockRequestBody.from_dict(submit_ip_block_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


