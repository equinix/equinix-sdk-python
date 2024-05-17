# BgpConfigRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | Autonomous System Number for local BGP deployment. | 
**deployment_type** | **str** | Wether the BGP deployment is local or global. Local deployments are configured immediately. Global deployments will need to be reviewed by Equinix Metal engineers. | 
**href** | **str** |  | [optional] 
**md5** | **str** | The plaintext password to share between BGP neighbors as an MD5 checksum: * must be 10-20 characters long * may not include punctuation * must be a combination of numbers and letters * must contain at least one lowercase, uppercase, and digit character  | [optional] 
**use_case** | **str** | A use case explanation (necessary for global BGP request review). | [optional] 

## Example

```python
from equinix_metal.models.bgp_config_request_input import BgpConfigRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of BgpConfigRequestInput from a JSON string
bgp_config_request_input_instance = BgpConfigRequestInput.from_json(json)
# print the JSON string representation of the object
print(BgpConfigRequestInput.to_json())

# convert the object into a dict
bgp_config_request_input_dict = bgp_config_request_input_instance.to_dict()
# create an instance of BgpConfigRequestInput from a dict
bgp_config_request_input_form_dict = bgp_config_request_input.from_dict(bgp_config_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


