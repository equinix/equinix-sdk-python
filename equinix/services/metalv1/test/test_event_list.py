# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.event_list import EventList

class TestEventList(unittest.TestCase):
    """EventList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventList:
        """Test EventList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventList`
        """
        model = EventList()
        if include_optional:
            return EventList(
                events = [
                    equinix.services.metalv1.models.event.Event(
                        body = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '', 
                        id = '', 
                        interpolated = '', 
                        ip = '', 
                        modified_by = equinix.services.metalv1.models.modified_by.modified_by(), 
                        relationships = [
                            equinix.services.metalv1.models.href.Href(
                                href = '', )
                            ], 
                        state = '', 
                        type = '', )
                    ],
                href = '',
                meta = equinix.services.metalv1.models.meta.Meta(
                    current_page = 56, 
                    first = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    href = '', 
                    last = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    last_page = 56, 
                    next = , 
                    previous = , 
                    self = , 
                    total = 56, )
            )
        else:
            return EventList(
        )
        """

    def testEventList(self):
        """Test EventList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
