# DeviceCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_pxe** | **bool** | When true, devices with a &#x60;custom_ipxe&#x60; OS will always boot to iPXE. The default setting of false ensures that iPXE will be used on only the first boot. | [optional] 
**billing_cycle** | **str** | The billing cycle of the device. | [optional] 
**customdata** | **Dict[str, object]** | Customdata is an arbitrary JSON value that can be accessed via the metadata service. | [optional] 
**description** | **str** | Any description of the device or how it will be used. This may be used to inform other API consumers with project access. | [optional] 
**features** | **List[str]** | The features attribute allows you to optionally specify what features your server should have.  In the API shorthand syntax, all features listed are &#x60;required&#x60;:  &#x60;&#x60;&#x60; { \&quot;features\&quot;: [\&quot;tpm\&quot;] } &#x60;&#x60;&#x60;  Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a &#x60;preferred&#x60; value. The request will not fail if we have no servers with that feature in our inventory. The API offers an alternative syntax for mixing preferred and required features:  &#x60;&#x60;&#x60; { \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot;, \&quot;raid\&quot;: \&quot;preferred\&quot; } } &#x60;&#x60;&#x60;  The request will only fail if there are no available servers matching the required &#x60;tpm&#x60; criteria. | [optional] 
**hardware_reservation_id** | **str** | The Hardware Reservation UUID to provision. Alternatively, &#x60;next-available&#x60; can be specified to select from any of the available hardware reservations. An error will be returned if the requested reservation option is not available.  See [Reserved Hardware](https://deploy.equinix.com/developers/docs/metal/deploy/reserved/) for more details. | [optional] 
**hostname** | **str** | The hostname to use within the operating system. The same hostname may be used on multiple devices within a project. | [optional] 
**href** | **str** |  | [optional] 
**ip_addresses** | [**List[IPAddress]**](IPAddress.md) | The &#x60;ip_addresses attribute will allow you to specify the addresses you want created with your device.  The default value configures public IPv4, public IPv6, and private IPv4.  Private IPv4 address is required. When specifying &#x60;ip_addresses&#x60;, one of the array items must enable private IPv4.  Some operating systems require public IPv4 address. In those cases you will receive an error message if public IPv4 is not enabled.  For example, to only configure your server with a private IPv4 address, you can send &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }] }&#x60;.  It is possible to request a subnet size larger than a &#x60;/30&#x60; by assigning addresses using the UUID(s) of ip_reservations in your project.  For example, &#x60;{ \&quot;ip_addresses\&quot;: [..., {\&quot;address_family\&quot;: 4, \&quot;public\&quot;: true, \&quot;ip_reservations\&quot;: [\&quot;uuid1\&quot;, \&quot;uuid2\&quot;]}] }&#x60;  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or proxy through another server in the project with public IPs enabled. | [optional] [default to [{"address_family":4,"public":true},{"address_family":4,"public":false},{"address_family":6,"public":true}]]
**ipxe_script_url** | **str** | When set, the device will chainload an iPXE Script at boot fetched from the supplied URL.  See [Custom iPXE](https://deploy.equinix.com/developers/docs/metal/operating-systems/custom-ipxe/) for more details. | [optional] 
**locked** | **bool** | Whether the device should be locked, preventing accidental deletion. | [optional] [default to False]
**network_frozen** | **bool** | If true, this instance can not be converted to a different network type. | [optional] 
**no_ssh_keys** | **bool** | Overrides default behaviour of attaching all of the organization members ssh keys and project ssh keys to device if no specific keys specified | [optional] [default to False]
**operating_system** | **str** | The slug of the operating system to provision. Check the Equinix Metal operating system documentation for rules that may be imposed per operating system, including restrictions on IP address options and device plans. | 
**plan** | **str** | The slug of the device plan to provision. | 
**private_ipv4_subnet_size** | **int** | Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. | [optional] 
**project_ssh_keys** | **List[str]** | A list of UUIDs identifying the device parent project that should be authorized to access this device (typically via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.  If no SSH keys are specified (&#x60;user_ssh_keys&#x60;, &#x60;project_ssh_keys&#x60;, and &#x60;ssh_keys&#x60; are all empty lists or omitted), all parent project keys, parent project members keys and organization members keys will be included. This behaviour can be changed with &#39;no_ssh_keys&#39; option to omit any SSH key being added.  | [optional] 
**public_ipv4_subnet_size** | **int** | Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request. | [optional] 
**spot_instance** | **bool** | Create a spot instance. Spot instances are created with a maximum bid price. If the bid price is not met, the spot instance will be terminated as indicated by the &#x60;termination_time&#x60; field. | [optional] 
**spot_price_max** | **float** | The maximum amount to bid for a spot instance. | [optional] 
**ssh_keys** | [**List[SSHKeyInput]**](SSHKeyInput.md) | A list of new or existing project ssh_keys that should be authorized to access this device (typically via /root/.ssh/authorized_keys). These keys will also appear in the device metadata.  These keys are added in addition to any keys defined by   &#x60;project_ssh_keys&#x60; and &#x60;user_ssh_keys&#x60;.  | [optional] 
**storage** | [**Storage**](Storage.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**termination_time** | **datetime** | When the device will be terminated. If you don&#39;t supply timezone info, the timestamp is assumed to be in UTC.  This is commonly set in advance for ephemeral spot market instances but this field may also be set with on-demand and reservation instances to automatically delete the resource at a given time. The termination time can also be used to release a hardware reservation instance at a given time, keeping the reservation open for other uses.  On a spot market device, the termination time will be set automatically when outbid.  | [optional] 
**user_ssh_keys** | **List[str]** | A list of UUIDs identifying the users that should be authorized to access this device (typically via /root/.ssh/authorized_keys).  These keys will also appear in the device metadata.  The users must be members of the project or organization.  If no SSH keys are specified (&#x60;user_ssh_keys&#x60;, &#x60;project_ssh_keys&#x60;, and &#x60;ssh_keys&#x60; are all empty lists or omitted), all parent project keys, parent project members keys and organization members keys will be included. This behaviour can be changed with &#39;no_ssh_keys&#39; option to omit any SSH key being added.  | [optional] 
**userdata** | **str** | The userdata presented in the metadata service for this device.  Userdata is fetched and interpreted by the operating system installed on the device. Acceptable formats are determined by the operating system, with the exception of a special iPXE enabling syntax which is handled before the operating system starts.  See [Server User Data](https://deploy.equinix.com/developers/docs/metal/server-metadata/user-data/) and [Provisioning with Custom iPXE](https://deploy.equinix.com/developers/docs/metal/operating-systems/custom-ipxe/#provisioning-with-custom-ipxe) for more details. | [optional] 

## Example

```python
from equinix_metal.models.device_create_input import DeviceCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceCreateInput from a JSON string
device_create_input_instance = DeviceCreateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceCreateInput.to_json())

# convert the object into a dict
device_create_input_dict = device_create_input_instance.to_dict()
# create an instance of DeviceCreateInput from a dict
device_create_input_form_dict = device_create_input.from_dict(device_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


