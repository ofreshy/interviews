"""

Which dish to sell?

Nory has decided to help its clients, to find what is the best dish to sell for a particular diner;

Each resturant has several dishes on its menu, each of which is represented by several fields as can be seen in the
Dish class below:


>>> class Dish(object):
>>>    def __init__(self, keywords:list, is_special:bool, price:float):

         :param keywords: a list of key words that are associated with the dish, such as VEGETERIAN, LIGHT, CARB_FREE etc
         :param is_special: if this is a special dish of the day
         :param price: the dish price as a float number


And a Diner is a simple class that contains a list of keywords

>>> class Diner(object):

>>>    def __init__(self, keywords:list):
         :param keywords: a list of key words that are associated with the dish, such as VEGETERIAN, LIGHT, CARB_FREE etc


The Nory algorithm ranks the match between a dish and a diner by three elements.
 These are listed below in decreasing order
- The more there are shared keywords between a dish and a diner then the higher the dish ranks
- If the dish is a special then the higher it ranks
- The pricier the dish then the higher it ranks

So, say that you have the following dishes
dish1 = <Dish : keywords=['MEAT'], is_special=False, price=15.0>
dish2 = <Dish : keywords=['VEGATERIAN'], is_special=False, price=11.0>
dish3 = <Dish : keywords=['MEAT'], is_special=True, price=8.0>

and the following diners
diner1 = <Diner : keywords=['VEGATERIAN']>
diner2 = <Diner : keywords=['MEAT']>

Then dish2 would be ranked highest for diner1 as it shares the same keyword VEGATERIAN whereas the other dishes don't.
Conversely, dish3 would be ranked highest for diner2 as it has the MEAT keyword and also is a special.


Task, implement the function recommend_dish() which takes a list of dishes and a diner,
and recommends the highest most ranking dish to this diner.

Assume no ties between dishes.

You can add methods on the classes as you see fit.
"""


class Diner(object):
    def __init__(self, keywords: list):
        self.keywords = keywords


class Dish(object):
    def __init__(self, keywords: list, is_special: bool, price: float):
        """
        :param keywords: a list of key words that are associated with the dish, such as VEGETARIAN, LIGHT, CARB_FREE etc
        :param is_special: if this is a special dish of the day
        :param price: the dish price as a float number
        """
        self.keywords = keywords
        self.is_special = is_special
        self.price = price

    def __str__(self):
        pattern = "[Dish : keywords={keywords}, is_special={is_special}, price={price}]"
        return pattern.format(
            keywords=self.keywords,
            is_special=self.is_special,
            price=self.price,
        )


def recommend_dish(dishes, diner):
    """
    :param dishes: list of Dish objects
    :param diner: a diner object
    :return: the most recommended dish by suitability, specials and price.
    """
    def rank(dish: Dish):
        suitability = len(set(diner.keywords) & set(dish.keywords))
        return suitability, int(dish.is_special), dish.price

    return sorted([d for d in dishes], key=rank)[-1]


dish1 = Dish(keywords=["A"], is_special=False, price=10.00)
dish2 = Dish(keywords=["D"], is_special=False, price=10.00)
dish3 = Dish(keywords=["A"], is_special=True, price=10.00)
dish4 = Dish(keywords=["A"], is_special=True, price=11.00)

dish5 = Dish(keywords=["A", "B", "D"], is_special=True, price=10.00)
dish6 = Dish(keywords=["A", "B", "E"], is_special=True, price=11.00)

diner1 = Diner(["A"])

# recommend one with most suitable keywords
assert recommend_dish([dish1, dish2], diner1) == dish1

# break keywords ties by is_special
assert recommend_dish([dish1, dish3], diner1) == dish3

# break keywords and is_special ties by price
assert recommend_dish([dish3, dish4], diner1) == dish4

# count keywords when more than one overlap
diner2 = Diner(["A", "E"])
assert recommend_dish([dish5, dish6], diner2) == dish6
