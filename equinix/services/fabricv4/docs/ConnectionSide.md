# ConnectionSide

Connection configuration object for each side of multi-segment connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | [**ServiceToken**](ServiceToken.md) |  | [optional] 
**access_point** | [**AccessPoint**](AccessPoint.md) |  | [optional] 
**internet_access** | [**InternetAccess**](InternetAccess.md) |  | [optional] 
**company_profile** | [**ConnectionCompanyProfile**](ConnectionCompanyProfile.md) |  | [optional] 
**invitation** | [**ConnectionInvitation**](ConnectionInvitation.md) |  | [optional] 
**additional_info** | [**List[ConnectionSideAdditionalInfo]**](ConnectionSideAdditionalInfo.md) | Any additional information, which is not part of connection metadata or configuration | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_side import ConnectionSide

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionSide from a JSON string
connection_side_instance = ConnectionSide.from_json(json)
# print the JSON string representation of the object
print(ConnectionSide.to_json())

# convert the object into a dict
connection_side_dict = connection_side_instance.to_dict()
# create an instance of ConnectionSide from a dict
connection_side_form_dict = connection_side.from_dict(connection_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


