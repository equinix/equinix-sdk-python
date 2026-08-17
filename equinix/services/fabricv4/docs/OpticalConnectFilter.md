# OpticalConnectFilter

A single condition, or a group of conditions combined with logical OR.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/name&#x60; - Connection name  * &#x60;/uuid&#x60; - Connection uuid  * &#x60;/type&#x60; - type  * &#x60;/state&#x60; - state  * &#x60;/bandwidth&#x60; - Bandwidth  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;[NOT] BETWEEN&#x60; - (not) between  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[OpticalConnectSimpleExpression]**](OpticalConnectSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_filter import OpticalConnectFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectFilter from a JSON string
optical_connect_filter_instance = OpticalConnectFilter.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectFilter.to_json())

# convert the object into a dict
optical_connect_filter_dict = optical_connect_filter_instance.to_dict()
# create an instance of OpticalConnectFilter from a dict
optical_connect_filter_from_dict = OpticalConnectFilter.from_dict(optical_connect_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


