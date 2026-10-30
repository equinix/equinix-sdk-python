# CreateAsnRequest

Create ASN request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**Project**](Project.md) |  | 
**number** | **int** | ASN number used for public ASN creation. | [optional] 
**rir_region** | [**AsnRirRegion**](AsnRirRegion.md) |  | [optional] 
**ownership_challenge_details** | [**AsnOwnershipChallengeDetails**](AsnOwnershipChallengeDetails.md) |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**range** | [**AsnRange**](AsnRange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.create_asn_request import CreateAsnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAsnRequest from a JSON string
create_asn_request_instance = CreateAsnRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAsnRequest.to_json())

# convert the object into a dict
create_asn_request_dict = create_asn_request_instance.to_dict()
# create an instance of CreateAsnRequest from a dict
create_asn_request_from_dict = CreateAsnRequest.from_dict(create_asn_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


