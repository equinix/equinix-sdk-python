# StreamFilterSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/subject&#x60; - subject  * &#x60;/type&#x60; - type  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;in&#x60; - in  * &#x60;LIKE&#x60; - case-sensitive like  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** | ### Supported event or metric names to use on filters with property /type:   * &#x60;*&#x60; - all events or metrics   * &#x60;equinix.fabric.port.*&#x60; - port events or metrics   * &#x60;equinix.fabric.connection.*&#x60; - connection events or metrics   * &#x60;equinix.fabric.router.*&#x60; - cloud router events   * &#x60;equinix.fabric.metro.*&#x60; - metro metrics   * &#x60;equinix.fabric.network.*&#x60; - network events   * &#x60;equinix.fabric.service_token.*&#x60; - service token events   * &#x60;equinix.network_edge.*&#x60; - network edge events   * &#x60;equinix.network_edge.acl.*&#x60; - network edge acl events   * &#x60;equinix.network_edge.device.*&#x60; - network edge device events   * &#x60;equinix.access_manager.*&#x60; - identity access manager events   * &#x60;equinix.access_manager.user.role.*&#x60; - identity access manager user role events ### Supported event or metric names to use on filters with property /subject:   * &#x60;*&#x60; - all events or metrics   * &#x60;/fabric/v4/ports/&lt;uuid&gt;&#x60; - port events or metrics   * &#x60;/fabric/v4/connections/&lt;uuid&gt;&#x60; - connection events or metrics   * &#x60;/fabric/v4/routers/&lt;uuid&gt;&#x60; - cloud router events   * &#x60;/fabric/v4/metros/&lt;metroCode&gt;&#x60; - metro metrics   * &#x60;/fabric/v4/networks/&lt;uuid&gt;&#x60; - network events   * &#x60;/fabric/v4/tokens/&lt;uuid&gt;&#x60; - service token events   * &#x60;/ne/v1/acl/&lt;uuid&gt;&#x60; - network edge acl events   * &#x60;/ne/v1/devices/&lt;uuid&gt;&#x60; - network edge device events   * &#x60;/am/v2/users/&lt;uuid&gt;/roleAssignments/&lt;uuid&gt;&#x60; - identity access manager events  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_filter_simple_expression import StreamFilterSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of StreamFilterSimpleExpression from a JSON string
stream_filter_simple_expression_instance = StreamFilterSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(StreamFilterSimpleExpression.to_json())

# convert the object into a dict
stream_filter_simple_expression_dict = stream_filter_simple_expression_instance.to_dict()
# create an instance of StreamFilterSimpleExpression from a dict
stream_filter_simple_expression_from_dict = StreamFilterSimpleExpression.from_dict(stream_filter_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


