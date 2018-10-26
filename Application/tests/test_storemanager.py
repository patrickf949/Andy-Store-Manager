import os
import pytest
from ..models.products import Products
from ..models.accounts import Accounts
from ..models.records import Records


class TestStoreManager():
	
	def test_creation(self):
		"""
		initialise objects
		"""
		self.products = Products()
		self.accounts = Accounts()
		self.records = Records()
		assert isinstance(self.products, Products)== True
		assert isinstance(self.records, Records)==True
		assert isinstance(self.accounts, Accounts)==True

#products
	def test_addProduct(self):
		"""
		test addition of product
		params: n/a
		returns: n/a
		"""
		self.products = Products('burgers', 120,10,1000)
		self.assertTrue(self.products.addProduct())
		self.assertFalse(self.products.addProduct())

	def test_deleteProduct(self):
		"""
		Test deletion of a product
		params: n/a
		returns: n/a
		"""
		self.products = Products('burgers',120,10,1000)
		# assert self.products.

	def test_deleteAllProducts(self):
		"""
		Test deletion of all Products
		params: n/a
		returns: n/a
		"""
		pass


	def test_updateExistingProduct(self):
		"""
		test update of product
		params: n/a
		returns: n/a
		"""
		pass
	

	def test_viewAllProducts(self):
		"""
		Test if all products can be viewed
		params: n/a
		returns: n/a
		"""
		pass
	

#accounts
	def test_addAccount(self):
		"""
		Test that an account can be added
		params: n/a
		returns: n/a
		"""
		pass


	def test_deleteAllAttendantAccounts(self):
		"""
		Test that all attendant accounts can be deleted
		params: n/a
		returns: n/a
		"""
		pass


	def test_updateExistingAccount(self):
		"""
		test that an existing account can be updated according to user preferences
		params: n/a
		returns: n/a
		"""
		pass


	@pytest.mark.skip(reason="no way of currently testing this")
	def test_methodThatMayNotBeTestable(self):
		pass


	def tearDown(self):
		"""
		Tear Down will destroy any objects that need to be destroyed at that point
		"""
		pass