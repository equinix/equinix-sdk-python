# CrossConnectEndCustomer

End customer details for the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_disclosed** | **bool** | Indicates if the end customer is disclosed. | [optional] 
**name** | **str** | End customer name. | [optional] 
**mdm_id** | **str** | Master Data Management identifier of the end customer, as held by Equinix.  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_end_customer import CrossConnectEndCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectEndCustomer from a JSON string
cross_connect_end_customer_instance = CrossConnectEndCustomer.from_json(json)
# print the JSON string representation of the object
print(CrossConnectEndCustomer.to_json())

# convert the object into a dict
cross_connect_end_customer_dict = cross_connect_end_customer_instance.to_dict()
# create an instance of CrossConnectEndCustomer from a dict
cross_connect_end_customer_from_dict = CrossConnectEndCustomer.from_dict(cross_connect_end_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


