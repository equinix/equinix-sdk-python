# CloudRouterSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/project/projectId&#x60; - project id (mandatory)  * &#x60;/name&#x60; - Fabric Cloud Router name  * &#x60;/uuid&#x60; - Fabric Cloud Router uuid  * &#x60;/state&#x60; - Fabric Cloud Router status  * &#x60;/location/metroCode&#x60; - Fabric Cloud Router metro code  * &#x60;/location/metroName&#x60; - Fabric Cloud Router metro name  * &#x60;/package/code&#x60; - Fabric Cloud Router package  * &#x60;/*&#x60; - all-category search  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;[NOT] BETWEEN&#x60; - (not) between  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_simple_expression import CloudRouterSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterSimpleExpression from a JSON string
cloud_router_simple_expression_instance = CloudRouterSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterSimpleExpression.to_json())

# convert the object into a dict
cloud_router_simple_expression_dict = cloud_router_simple_expression_instance.to_dict()
# create an instance of CloudRouterSimpleExpression from a dict
cloud_router_simple_expression_form_dict = cloud_router_simple_expression.from_dict(cloud_router_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


