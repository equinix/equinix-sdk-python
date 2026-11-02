# AsnAsset

Asset associated with ASN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**service** | [**AsnAssetService**](AsnAssetService.md) |  | [optional] 
**announcing_metro** | **str** |  | [optional] 
**ip_blocks** | [**List[AsnAssetIpBlockRef]**](AsnAssetIpBlockRef.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_asset import AsnAsset

# TODO update the JSON string below
json = "{}"
# create an instance of AsnAsset from a JSON string
asn_asset_instance = AsnAsset.from_json(json)
# print the JSON string representation of the object
print(AsnAsset.to_json())

# convert the object into a dict
asn_asset_dict = asn_asset_instance.to_dict()
# create an instance of AsnAsset from a dict
asn_asset_from_dict = AsnAsset.from_dict(asn_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


