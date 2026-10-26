# AsnOwnershipChallengeRpki


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Challenge message to sign | [optional] 
**signature** | **str** | Signed challenge value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_ownership_challenge_rpki import AsnOwnershipChallengeRpki

# TODO update the JSON string below
json = "{}"
# create an instance of AsnOwnershipChallengeRpki from a JSON string
asn_ownership_challenge_rpki_instance = AsnOwnershipChallengeRpki.from_json(json)
# print the JSON string representation of the object
print(AsnOwnershipChallengeRpki.to_json())

# convert the object into a dict
asn_ownership_challenge_rpki_dict = asn_ownership_challenge_rpki_instance.to_dict()
# create an instance of AsnOwnershipChallengeRpki from a dict
asn_ownership_challenge_rpki_from_dict = AsnOwnershipChallengeRpki.from_dict(asn_ownership_challenge_rpki_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


