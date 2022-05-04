import unittest
import asyncio
import time
from faker import Faker 
import tests as my

fak=Faker()


class U_Tests(unittest.TestCase):
    def test_int_hash(self):
        self.assertEqual(my.get_hash(123),
        'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3')
        
    def test_str_hash(self):
        self.assertEqual(my.get_hash(123.2),None)
        
    def test_dic_hash(self):
        self.assertEqual(my.get_hash({'dic':'\naaa'}),None)
        
    def test_tuple_ret_main(self):
        self.b=tuple((
            fak.name(),
            fak.job(),
            fak.random_int(min=1000, max=500000)
            ))
        self.a=my.main(self.b)
        self.assertCountEqual(self.a, self.b, 
            msg="тест с кортежем")
        
    def test_list_ret_main(self):
        self.b=list((
            fak.name(),
            fak.job(),
            fak.random_int(min=1000, max=500000)
            ))
        self.a=my.main(self.b)
        self.assertCountEqual(self.a, self.b, 
            msg="тест с листом")
        
    def test_set_ret_main(self):
        self.b=set((
            fak.name(),
            fak.job(),
            fak.random_int(min=1000, max=500000)
            ))
        self.a=my.main(self.b)
        self.assertCountEqual(self.a, self.b, 
            msg="тест с набором")
        
    def test_dict_ret_main(self):
        self.b={
                'Name':fak.name(),
                'Job':fak.job(),
                'Cash':fak.random_int(min=1000, max=500000)}
        self.a=my.main(self.b)
        self.assertCountEqual(self.a, self.b.values(), 
            msg="тест со словарем")
        
    def test_dict_ret_cor(self):
        self.b={
                'Name':fak.name(),
                'Job':fak.job(),
                'Cash':fak.random_int(min=1000, max=500000)}
        self.loop=asyncio.get_event_loop()
        self.a=self.loop.run_until_complete(
            my.corut(self.b))
        self.assertCountEqual(self.a, self.b.values(), 
            msg="тест со словарем")
        
    def test_list_ret_cor(self):
        self.b=list((
            fak.name(),
            fak.job(),
            fak.random_int(min=1000, max=500000)
            ))
        self.loop=asyncio.get_event_loop()
        self.a=self.loop.run_until_complete(
            my.corut(self.b))
        self.assertCountEqual(self.a, self.b, 
            msg="тест с листом")
        
    def test_set_ret_cor(self):
        self.b=set((
            fak.name(),
            fak.job(),
            fak.random_int(min=1000, max=500000)
            ))
        self.loop=asyncio.get_event_loop()
        self.a=self.loop.run_until_complete(
            my.corut(self.b))
        self.assertCountEqual(self.a, self.b, 
            msg="тест с набором")

    def test_tuple_ret_cor(self):
        self.b=tuple((
            fak.name(),
            fak.job(),
            fak.random_int(min=1000, max=500000)
            ))
        self.loop=asyncio.get_event_loop()
        self.a=self.loop.run_until_complete(
            my.corut(self.b))
        self.assertCountEqual(self.a, self.b, 
            msg="тест с кортежем")
        
        def test_float_ret_cor(self):
            self.b=123.5
            self.loop=asyncio.get_event_loop()
            self.a=self.loop.run_until_complete(
                my.corut(self.b))
            self.assertEqual(self.a, None, msg="тест на нон")
        
        
        

        def test_time(self):
            self.start_time = time.time()
            self.test_list_ret_cor(self)
            self.assertLess(time.time() - self.start_time,5)
        def test_prtn(self):
            self.start_time = time.time()
            self.b=fak.name()
            self.a=my.prtn(self.b)
            self.assertLess(time.time() - self.start_time,5, 
                msg="тест на возврат строки за время меньше 5 сек")
            self.assertEqual(self.a, self.b, 
                msg="тест на возврат строки за время меньше 5 сек")
                
"""if __name__=='__main__':
    unittest.main()"""
