# ResourceSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | ### Supported metric names to use on filters with property /subject:   * &#x60;/fabric/v4/ports/&lt;uuid&gt;&#x60; - port metrics   * &#x60;/fabric/v4/connections/&lt;uuid&gt;&#x60; - connection metrics   * &#x60;/fabric/v4/metros/&lt;metroCode&gt;&#x60; - metro latency metrics  | 

## Example

```python
from equinix.services.fabricv4.models.resource_selector import ResourceSelector

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSelector from a JSON string
resource_selector_instance = ResourceSelector.from_json(json)
# print the JSON string representation of the object
print(ResourceSelector.to_json())

# convert the object into a dict
resource_selector_dict = resource_selector_instance.to_dict()
# create an instance of ResourceSelector from a dict
resource_selector_from_dict = ResourceSelector.from_dict(resource_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


