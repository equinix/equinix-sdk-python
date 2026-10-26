# AsnOwnershipChallengeLoa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_format** | **str** | Document content format | [optional] 
**document_reference** | **str** | Document reference identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_ownership_challenge_loa import AsnOwnershipChallengeLoa

# TODO update the JSON string below
json = "{}"
# create an instance of AsnOwnershipChallengeLoa from a JSON string
asn_ownership_challenge_loa_instance = AsnOwnershipChallengeLoa.from_json(json)
# print the JSON string representation of the object
print(AsnOwnershipChallengeLoa.to_json())

# convert the object into a dict
asn_ownership_challenge_loa_dict = asn_ownership_challenge_loa_instance.to_dict()
# create an instance of AsnOwnershipChallengeLoa from a dict
asn_ownership_challenge_loa_from_dict = AsnOwnershipChallengeLoa.from_dict(asn_ownership_challenge_loa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


