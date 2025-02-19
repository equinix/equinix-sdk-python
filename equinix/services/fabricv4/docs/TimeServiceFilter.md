# TimeServiceFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/project/projectId&#x60; - project id (mandatory)  * &#x60;/name&#x60; - Precision Time Service name  * &#x60;/uuid&#x60; - Precision Time Service uuid  * &#x60;/type&#x60; - Precision Time Service protocol  * &#x60;/state&#x60; - Precision Time Service status  * &#x60;/account/accountNumber&#x60; - Precision Time Service account number  * &#x60;/package/code&#x60; - Precision Time Service package  * &#x60;/*&#x60; - all-category search  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;[NOT] BETWEEN&#x60; - (not) between  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[TimeServiceSimpleExpression]**](TimeServiceSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_filter import TimeServiceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServiceFilter from a JSON string
time_service_filter_instance = TimeServiceFilter.from_json(json)
# print the JSON string representation of the object
print(TimeServiceFilter.to_json())

# convert the object into a dict
time_service_filter_dict = time_service_filter_instance.to_dict()
# create an instance of TimeServiceFilter from a dict
time_service_filter_from_dict = TimeServiceFilter.from_dict(time_service_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


