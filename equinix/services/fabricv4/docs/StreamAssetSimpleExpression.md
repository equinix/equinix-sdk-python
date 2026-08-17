# StreamAssetSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/uuid&#x60; - Asset uuid (&#x60;&#x3D;&#x60; and &#x60;IN&#x60; only)  * &#x60;/streamUuid&#x60; - Stream uuid (&#x60;&#x3D;&#x60; and &#x60;IN&#x60; only)  * &#x60;/attachmentStatus&#x60; - Asset attachment status (&#x60;&#x3D;&#x60;, &#x60;IN&#x60;, and &#x60;NOT IN&#x60;)  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;IN&#x60; - in  * &#x60;NOT IN&#x60; - not in  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset_simple_expression import StreamAssetSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetSimpleExpression from a JSON string
stream_asset_simple_expression_instance = StreamAssetSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(StreamAssetSimpleExpression.to_json())

# convert the object into a dict
stream_asset_simple_expression_dict = stream_asset_simple_expression_instance.to_dict()
# create an instance of StreamAssetSimpleExpression from a dict
stream_asset_simple_expression_from_dict = StreamAssetSimpleExpression.from_dict(stream_asset_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


