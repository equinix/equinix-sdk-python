# MetroInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**metro** | **str** | Metro code or ID of where the device should be provisioned in, or it can be instructed to create the device in the best available metro with &#x60;{ \&quot;metro\&quot;: \&quot;any\&quot; }&#x60;. The special metro value of any means anywhere, any metro. When any is chosen in the request, the metro location is picked per our scheduling algorithms that favor the following factors: hardware reservation location (if requesting reserved hardware), ip reservations, spot instances, etc. The any keyword *does not* optimize for cost, this means that usage costs (instance, transfer, other features dependent on location) will vary. Please check metro value in response to see where the device was created. Either metro or facility must be provided. | 

## Example

```python
from equinix_metal.models.metro_input import MetroInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetroInput from a JSON string
metro_input_instance = MetroInput.from_json(json)
# print the JSON string representation of the object
print(MetroInput.to_json())

# convert the object into a dict
metro_input_dict = metro_input_instance.to_dict()
# create an instance of MetroInput from a dict
metro_input_form_dict = metro_input.from_dict(metro_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


