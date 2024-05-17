# InterconnectionUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**mode** | **str** | The mode of the interconnection (only relevant to Dedicated Ports). Shared connections won&#39;t have this field. Can be either &#39;standard&#39; or &#39;tunnel&#39;.   The default mode of an interconnection on a Dedicated Port is &#39;standard&#39;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] 
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_update_input import InterconnectionUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionUpdateInput from a JSON string
interconnection_update_input_instance = InterconnectionUpdateInput.from_json(json)
# print the JSON string representation of the object
print(InterconnectionUpdateInput.to_json())

# convert the object into a dict
interconnection_update_input_dict = interconnection_update_input_instance.to_dict()
# create an instance of InterconnectionUpdateInput from a dict
interconnection_update_input_form_dict = interconnection_update_input.from_dict(interconnection_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


