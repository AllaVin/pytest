# HW 6: Automated Test with Page Object Model

## Task
Automated test for https://www.saucedemo.com using POM.

### Steps:
1. Login as `standard_user`
2. Add to cart:
   - Sauce Labs Backpack
   - Sauce Labs Bolt T-Shirt
   - Sauce Labs Onesie
3. Proceed to checkout
4. Fill in:
   - First Name
   - Last Name
   - Postal Code
5. Verify total: `$58.29`
6. Test must use Page Object Model and run independently.

## Run
```bash
pip install -r requirements.txt
pytest tests/test_checkout.py -v
```
