# CloudRouterActionsSearchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/type&#x60; - type of update  * &#x60;/state&#x60; - action state  * &#x60;/connection/uuid&#x60; - connection uuid associated  * &#x60;/*&#x60; - all-category search  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;&gt;&#x60; - greater than  * &#x60;&gt;&#x3D;&#x60; - greater than or equal to  * &#x60;&lt;&#x60; - less than  * &#x60;&lt;&#x3D;&#x60; - less than or equal to  * &#x60;[NOT] BETWEEN&#x60; - (not) between  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;~*&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_actions_search_expression import CloudRouterActionsSearchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionsSearchExpression from a JSON string
cloud_router_actions_search_expression_instance = CloudRouterActionsSearchExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionsSearchExpression.to_json())

# convert the object into a dict
cloud_router_actions_search_expression_dict = cloud_router_actions_search_expression_instance.to_dict()
# create an instance of CloudRouterActionsSearchExpression from a dict
cloud_router_actions_search_expression_form_dict = cloud_router_actions_search_expression.from_dict(cloud_router_actions_search_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


