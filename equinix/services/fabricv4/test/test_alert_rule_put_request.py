# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.alert_rule_put_request import AlertRulePutRequest

class TestAlertRulePutRequest(unittest.TestCase):
    """AlertRulePutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertRulePutRequest:
        """Test AlertRulePutRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertRulePutRequest`
        """
        model = AlertRulePutRequest()
        if include_optional:
            return AlertRulePutRequest(
                name = '',
                description = '',
                enabled = True,
                metric_name = 'equinix.fabric.connection.bandwidth_tx.usage',
                resource_selector = equinix.services.fabricv4.models.resource_selector.ResourceSelector(
                    include = [
                        ''
                        ], ),
                operand = 'ABOVE',
                window_size = 'PT15M',
                warning_threshold = '',
                critical_threshold = ''
            )
        else:
            return AlertRulePutRequest(
        )
        """

    def testAlertRulePutRequest(self):
        """Test AlertRulePutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
