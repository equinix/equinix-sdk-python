# AsnAssetIpBlockRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**AsnAssetIpBlockRefType**](AsnAssetIpBlockRefType.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_asset_ip_block_ref import AsnAssetIpBlockRef

# TODO update the JSON string below
json = "{}"
# create an instance of AsnAssetIpBlockRef from a JSON string
asn_asset_ip_block_ref_instance = AsnAssetIpBlockRef.from_json(json)
# print the JSON string representation of the object
print(AsnAssetIpBlockRef.to_json())

# convert the object into a dict
asn_asset_ip_block_ref_dict = asn_asset_ip_block_ref_instance.to_dict()
# create an instance of AsnAssetIpBlockRef from a dict
asn_asset_ip_block_ref_from_dict = AsnAssetIpBlockRef.from_dict(asn_asset_ip_block_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


