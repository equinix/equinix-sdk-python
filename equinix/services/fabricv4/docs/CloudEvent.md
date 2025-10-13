# CloudEvent

Cloud Event object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | **str** | Cloud Event Open Telemetry specification | [optional] [readonly] 
**source** | **str** | Cloud Event source | [optional] 
**id** | **str** | Cloud Event identifier | [optional] 
**type** | **str** | Equinix supported event type | [optional] 
**subject** | **str** | Cloud Event subject | [optional] 
**time** | **datetime** | Cloud Event time the event occurred | [optional] 
**dataschema** | **str** | Cloud Event dataschema reference | [optional] 
**datacontenttype** | **str** | Cloud Event data content type | [optional] 
**severitynumber** | **str** | Cloud Event severity number | [optional] 
**severitytext** | **str** | Cloud Event severity text | [optional] 
**equinixalert** | **str** | Equinix alert | [optional] 
**equinixorganization** | **str** | Equinix organization identifier | [optional] 
**equinixproject** | **str** | Equinix project identifier | [optional] 
**authtype** | **str** | Cloud Event auth type | [optional] 
**authid** | **str** | Cloud Event user identifier | [optional] 
**traceparent** | **str** | Cloud Event traceparent | [optional] 
**tracestate** | **str** | Cloud Event tracestate | [optional] 
**data** | [**CloudEventData**](CloudEventData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_event import CloudEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CloudEvent from a JSON string
cloud_event_instance = CloudEvent.from_json(json)
# print the JSON string representation of the object
print(CloudEvent.to_json())

# convert the object into a dict
cloud_event_dict = cloud_event_instance.to_dict()
# create an instance of CloudEvent from a dict
cloud_event_from_dict = CloudEvent.from_dict(cloud_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


