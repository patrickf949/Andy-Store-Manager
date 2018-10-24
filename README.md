# Store-Manager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.
Test Badges
![Python 3.5](https://img.shields.io/badge/python-3.5+-blue.svg) ![PEP8](https://img.shields.io/badge/code%20style-pep8-blue.svg) ![pylint Score](https://mperlet.github.io/pybadge/badges/7.89.svg)
###Test Badges
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)[![Build Status](https://travis-ci.org/patrickf949/Store-Manager.svg?branch=ch-api-design)](https://travis-ci.org/patrickf949/Store-Manager)

#####Front end
| Page | Purpose | link |
| :---------------- | :---------------| :--------------- |
| Landing Page | First page viewed by user, contains login options, first being for store attendant and second being Admin Login | [Attendant Login](https://patrickf949.github.io/Store-Manager/UI/templates/) |
| Admin Dashboard | The Dashboard viewed by Admin on login, showing all Attendants and their information including total sales, sales worth which on click leads to the specified attendants profile. This page also inclueds important details such as total sales made, total sales worth.  | [Admin Dashboard](https://patrickf949.github.io/Store-Manager/UI/templates/admin_home.html) |
| Add Store Attendant | This is where an admin can add a new store attendant | [Add new Attendant](https://patrickf949.github.io/Store-Manager/UI/templates/signup.html) |
| Edit Store Attendant | Admin can edit a store attendant's information on this page | [Add new Attendant](https://patrickf949.github.io/Store-Manager/UI/templates/editattendant.html) |
| Add Product | The admin can add a product providing all necessary information such as the name, unit price, quantity in stock, minimum quantity acceptable in stock | [Add Product](https://patrickf949.github.io/Store-Manager/UI/templates/newproduct.html) |
| Edit Product | The admin can edit a product - when adding more stock,or changing price due to  inflation, or if a robbery occured - providing quantity of stock to be added or changing minimum quantity, name | [Edit Product](https://patrickf949.github.io/Store-Manager/UI/templates/editproduct.html) |
| Products | On this page, the admin can view all the available products in the inventory, plus their records, how many times they've been sold, their price, quantity, minimum quantity | [All products](https://patrickf949.github.io/Store-Manager/UI/templates/products.html) |
| All Sale Records | Admins can view all sale records for all the available store attendants basing on how recent the sales were made | [Sale Records](https://patrickf949.github.io/Store-Manager/UI/templates/all_records.html) |
| Sale Records | The admin page which shows all sale records in the system | [sale records](https://patrickf949.github.io/Store-Manager/UI/templates/records.html) |
| Store Attendant Dashboard | The Dashboard page for Store attendants, showing all available products in the inventory and also the store attendant's statistics, that is, total sales, total sales worth with links to add new cart and view records | [Attendant Dashboard](https://patrickf949.github.io/Store-Manager/UI/templates/attendant_home.html) |
| Cart | Store attendant creates a cart where he/she can add items for purchase orders | [new cart](https://patrickf949.github.io/Store-Manager/UI/templates/cart.html) |
| View Sales Records | Store attendant can view all his or her sales records but can not edit them | [View records](https://patrickf949.github.io/Store-Manager/UI/templates/attendant_records.html) |

####Technologies utilised
- HTML5/CSS
- Python 3
- Flask Framework
- pytest
