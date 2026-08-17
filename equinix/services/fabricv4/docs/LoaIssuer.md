# LoaIssuer

Issuer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the issuer contact. | [optional] 
**org_id** | **int** | Organization ID of the issuer. | [optional] 
**org_name** | **str** | Organization name of the issuer. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_issuer import LoaIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of LoaIssuer from a JSON string
loa_issuer_instance = LoaIssuer.from_json(json)
# print the JSON string representation of the object
print(LoaIssuer.to_json())

# convert the object into a dict
loa_issuer_dict = loa_issuer_instance.to_dict()
# create an instance of LoaIssuer from a dict
loa_issuer_from_dict = LoaIssuer.from_dict(loa_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


