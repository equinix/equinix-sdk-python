# AsnOwnershipChallengeDetails

Ownership challenge details for public ASN verification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AsnOwnershipChallengeType**](AsnOwnershipChallengeType.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.asn_ownership_challenge_details import AsnOwnershipChallengeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AsnOwnershipChallengeDetails from a JSON string
asn_ownership_challenge_details_instance = AsnOwnershipChallengeDetails.from_json(json)
# print the JSON string representation of the object
print(AsnOwnershipChallengeDetails.to_json())

# convert the object into a dict
asn_ownership_challenge_details_dict = asn_ownership_challenge_details_instance.to_dict()
# create an instance of AsnOwnershipChallengeDetails from a dict
asn_ownership_challenge_details_from_dict = AsnOwnershipChallengeDetails.from_dict(asn_ownership_challenge_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


