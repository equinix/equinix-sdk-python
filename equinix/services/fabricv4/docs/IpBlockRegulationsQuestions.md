# IpBlockRegulationsQuestions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_space_considered** | **bool** |  | 
**refused_previously** | **bool** |  | 
**returning_address_space** | **bool** |  | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_regulations_questions import IpBlockRegulationsQuestions

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockRegulationsQuestions from a JSON string
ip_block_regulations_questions_instance = IpBlockRegulationsQuestions.from_json(json)
# print the JSON string representation of the object
print(IpBlockRegulationsQuestions.to_json())

# convert the object into a dict
ip_block_regulations_questions_dict = ip_block_regulations_questions_instance.to_dict()
# create an instance of IpBlockRegulationsQuestions from a dict
ip_block_regulations_questions_from_dict = IpBlockRegulationsQuestions.from_dict(ip_block_regulations_questions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


