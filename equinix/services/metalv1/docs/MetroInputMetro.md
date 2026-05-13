# MetroInputMetro

Metro code or ID of where the device should be provisioned in, or it can be instructed to create the device in the best available metro with `{ \"metro\": \"any\" }`. The special metro value of any means anywhere, any metro. When any is chosen in the request, the metro location is picked per our scheduling algorithms that favor the following factors: hardware reservation location (if requesting reserved hardware), ip reservations, spot instances, etc. The any keyword *does not* optimize for cost, this means that usage costs (instance, transfer, other features dependent on location) will vary. Please check metro value in response to see where the device was created.  Additionally it is possible to set a prioritized location selection. For example `{ \"metro\": [\"m3\", \"m2\", \"any\"] }` can be used to prioritize `m3` and then `m2` before accepting `any` metro. If none of the metros provided have availability for the requested device the request will fail. Either metro or facility must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from equinix.services.metalv1.models.metro_input_metro import MetroInputMetro

# TODO update the JSON string below
json = "{}"
# create an instance of MetroInputMetro from a JSON string
metro_input_metro_instance = MetroInputMetro.from_json(json)
# print the JSON string representation of the object
print(MetroInputMetro.to_json())

# convert the object into a dict
metro_input_metro_dict = metro_input_metro_instance.to_dict()
# create an instance of MetroInputMetro from a dict
metro_input_metro_from_dict = MetroInputMetro.from_dict(metro_input_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


