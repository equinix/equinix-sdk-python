# AsnAssetService

Associated Internet Access Service reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**AsnAssetServiceType**](AsnAssetServiceType.md) |  | [optional] 
**uuid** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_asset_service import AsnAssetService

# TODO update the JSON string below
json = "{}"
# create an instance of AsnAssetService from a JSON string
asn_asset_service_instance = AsnAssetService.from_json(json)
# print the JSON string representation of the object
print(AsnAssetService.to_json())

# convert the object into a dict
asn_asset_service_dict = asn_asset_service_instance.to_dict()
# create an instance of AsnAssetService from a dict
asn_asset_service_from_dict = AsnAssetService.from_dict(asn_asset_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


