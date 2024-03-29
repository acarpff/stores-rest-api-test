from models.item import ItemModel
from models.store import StoreModel

from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [],
                             "The store's items lengh was not 0 even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 11.11, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test')
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')
            self.assertEqual(store.items.first().price, 11.11)

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'id': None,
            'items': [],
            'name': 'test'
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 11.11, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'id': 1,
                'items': [{'name': 'test_item','price': 11.11}],
                'name': 'test'
            }

            self.assertDictEqual(store.json(), expected)



































