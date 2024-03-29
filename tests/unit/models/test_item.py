from tests.unit.unit_base_test import UnitBaseTest

from models.item import ItemModel



class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test', 11.11, 1)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 11.11,
                         "The price of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test', 11.11, 1)
        expected = {
            'name': 'test',
            'price': 11.11
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
