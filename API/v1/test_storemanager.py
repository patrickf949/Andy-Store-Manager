import pytest
from products import Products
from accounts import Accounts
from records import Records


class TestStoreManager():
	
	def test_creation(self):
		self.products = Products()
		self.accounts = Accounts()
		self.records = Records()
		a = isinstance(self.products, Products)
		b = isinstance(self.records, Records)
		c = isinstance(self.accounts, Accounts)


	def test_addProduct(self):
		"""
		a
		params: n/a
		returns: n/a
		"""
		pass

	def test_deleteProduct(self):
		"""
		a
		params: n/a
		returns: n/a
		"""
		pass

	def test_updateExistingProduct(self):
		"""
		a
		params: n/a
		returns: n/a
		"""
		pass
	
	def test_viewAllProducts(self):
		"""
		Test if all products can 
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