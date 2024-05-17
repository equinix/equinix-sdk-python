# InterconnectionPortList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ports** | [**List[InterconnectionPort]**](InterconnectionPort.md) |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_port_list import InterconnectionPortList

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionPortList from a JSON string
interconnection_port_list_instance = InterconnectionPortList.from_json(json)
# print the JSON string representation of the object
print(InterconnectionPortList.to_json())

# convert the object into a dict
interconnection_port_list_dict = interconnection_port_list_instance.to_dict()
# create an instance of InterconnectionPortList from a dict
interconnection_port_list_form_dict = interconnection_port_list.from_dict(interconnection_port_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


