# Address

Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Address identifier | [optional] 
**street_nr** | **str** | Street number of address | [optional] 
**street_name** | **str** | Street name of address | [optional] 
**city** | **str** | City of address | [optional] 
**state_or_province** | **str** | State of address | [optional] 
**post_code** | **str** | Postal code of address | [optional] 
**country** | **str** | Country of address | [optional] 

## Example

```python
from equinix.services.fabricv4.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


