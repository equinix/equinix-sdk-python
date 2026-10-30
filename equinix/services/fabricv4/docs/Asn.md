# Asn

ASN Record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** | Unique identifier for the ASN record | [optional] 
**state** | [**AsnState**](AsnState.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**number** | **int** | Autonomous System Number | [optional] 
**rir_region** | [**AsnRirRegion**](AsnRirRegion.md) |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**range** | [**AsnRange**](AsnRange.md) |  | [optional] 
**ownership_challenge_details** | [**AsnOwnershipChallengeDetails**](AsnOwnershipChallengeDetails.md) |  | [optional] 
**change** | [**AsnChange**](AsnChange.md) |  | [optional] 
**assets** | [**List[AsnAsset]**](AsnAsset.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) | List of errors | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn import Asn

# TODO update the JSON string below
json = "{}"
# create an instance of Asn from a JSON string
asn_instance = Asn.from_json(json)
# print the JSON string representation of the object
print(Asn.to_json())

# convert the object into a dict
asn_dict = asn_instance.to_dict()
# create an instance of Asn from a dict
asn_from_dict = Asn.from_dict(asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


