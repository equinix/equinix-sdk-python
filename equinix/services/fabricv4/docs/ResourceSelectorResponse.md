# ResourceSelectorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | ### Supported metric names to use on filters with property /subject:   * &#x60;/fabric/v4/ports/&lt;uuid&gt;&#x60; - port metrics   * &#x60;/fabric/v4/connections/&lt;uuid&gt;&#x60; - connection metrics   * &#x60;/fabric/v4/metros/&lt;metroCode&gt;&#x60; - metro latency metrics  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.resource_selector_response import ResourceSelectorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSelectorResponse from a JSON string
resource_selector_response_instance = ResourceSelectorResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceSelectorResponse.to_json())

# convert the object into a dict
resource_selector_response_dict = resource_selector_response_instance.to_dict()
# create an instance of ResourceSelectorResponse from a dict
resource_selector_response_from_dict = ResourceSelectorResponse.from_dict(resource_selector_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


