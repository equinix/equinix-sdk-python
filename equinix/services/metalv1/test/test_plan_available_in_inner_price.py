# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.plan_available_in_inner_price import PlanAvailableInInnerPrice

class TestPlanAvailableInInnerPrice(unittest.TestCase):
    """PlanAvailableInInnerPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlanAvailableInInnerPrice:
        """Test PlanAvailableInInnerPrice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlanAvailableInInnerPrice`
        """
        model = PlanAvailableInInnerPrice()
        if include_optional:
            return PlanAvailableInInnerPrice(
                hour = 1.23,
                href = ''
            )
        else:
            return PlanAvailableInInnerPrice(
        )
        """

    def testPlanAvailableInInnerPrice(self):
        """Test PlanAvailableInInnerPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
