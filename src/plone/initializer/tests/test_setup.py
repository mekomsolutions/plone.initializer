# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from plone.initializer.testing import (
    PLONE_INITIALIZER_INTEGRATION_TESTING  # noqa: E501,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plone.initializer is properly installed."""

    layer = PLONE_INITIALIZER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.initializer is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.initializer'))

    def test_browserlayer(self):
        """Test that IPloneInitializerLayer is registered."""
        from plone.initializer.interfaces import (
            IPloneInitializerLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneInitializerLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_INITIALIZER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plone.initializer'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.initializer is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.initializer'))

    def test_browserlayer_removed(self):
        """Test that IPloneInitializerLayer is removed."""
        from plone.initializer.interfaces import \
            IPloneInitializerLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneInitializerLayer,
            utils.registered_layers())
