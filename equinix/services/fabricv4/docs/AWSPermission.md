# AWSPermission

Provides the AWS permission configuration for the orchestrator. This permission is used to manage the AWS resources and their access control. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSPermissionType**](AWSPermissionType.md) |  | 
**role_arn** | **str** |  | 
**region** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_permission import AWSPermission

# TODO update the JSON string below
json = "{}"
# create an instance of AWSPermission from a JSON string
aws_permission_instance = AWSPermission.from_json(json)
# print the JSON string representation of the object
print(AWSPermission.to_json())

# convert the object into a dict
aws_permission_dict = aws_permission_instance.to_dict()
# create an instance of AWSPermission from a dict
aws_permission_from_dict = AWSPermission.from_dict(aws_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


