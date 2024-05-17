# BgpConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | Autonomous System Number. ASN is required with Global BGP. With Local BGP the private ASN, 65000, is assigned. | [optional] 
**created_at** | **datetime** |  | [optional] 
**deployment_type** | **str** | In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space.  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**max_prefix** | **int** | The maximum number of route filters allowed per server | [optional] [default to 10]
**md5** | **str** | (Optional) Password for BGP session in plaintext (not a checksum) | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**ranges** | [**List[GlobalBgpRange]**](GlobalBgpRange.md) | The IP block ranges associated to the ASN (Populated in Global BGP only) | [optional] 
**requested_at** | **datetime** |  | [optional] 
**route_object** | **str** | Specifies AS-MACRO (aka AS-SET) to use when building client route filters | [optional] 
**sessions** | [**List[BgpSession]**](BgpSession.md) | The direct connections between neighboring routers that want to exchange routing information. | [optional] 
**status** | **str** | Status of the BGP Config. Status \&quot;requested\&quot; is valid only with the \&quot;global\&quot; deployment_type. | [optional] 

## Example

```python
from equinix_metal.models.bgp_config import BgpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BgpConfig from a JSON string
bgp_config_instance = BgpConfig.from_json(json)
# print the JSON string representation of the object
print(BgpConfig.to_json())

# convert the object into a dict
bgp_config_dict = bgp_config_instance.to_dict()
# create an instance of BgpConfig from a dict
bgp_config_form_dict = bgp_config.from_dict(bgp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


