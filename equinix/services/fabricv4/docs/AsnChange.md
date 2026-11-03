# AsnChange

Change reference for ASN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL path to the change event | [optional] 

## Example

```python
from equinix.services.fabricv4.models.asn_change import AsnChange

# TODO update the JSON string below
json = "{}"
# create an instance of AsnChange from a JSON string
asn_change_instance = AsnChange.from_json(json)
# print the JSON string representation of the object
print(AsnChange.to_json())

# convert the object into a dict
asn_change_dict = asn_change_instance.to_dict()
# create an instance of AsnChange from a dict
asn_change_from_dict = AsnChange.from_dict(asn_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


