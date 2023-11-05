from unittest import TestCase
from assignment import PizzaApp


class Test(TestCase):
    def test_total_slices(self):
        hungry = 2
        semiHungry = 2
        classic = 2
        self.assertEqual(14, PizzaApp.totalSlices(hungry, semiHungry, classic))

    def testLargeSizeRecommended(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        self.assertEqual(2, PizzaApp.recommendLargestSize(hungry, semiHungry, classic))

    def testMediumSizeRecommended(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        self.assertEqual(4, PizzaApp.recommendMediumSize(hungry, semiHungry, classic))

    def testSmallSizeRecommended(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        self.assertEqual(5, PizzaApp.recommendSmallSize(hungry, semiHungry, classic))

    def testLargePizzaSlicesLeft(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        totalSlices = PizzaApp.totalSlices(hungry, semiHungry, classic)
        totalBox = PizzaApp.recommendLargestSize(hungry, semiHungry, classic)
        self.assertEqual(0, PizzaApp.largePizzaSlicesLeft(totalSlices, totalBox))

    def testMediumSlicesLeft(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        totalSlices = PizzaApp.totalSlices(hungry, semiHungry, classic)
        totalBox = PizzaApp.recommendMediumSize(hungry, semiHungry, classic)
        self.assertEqual(4, PizzaApp.mediumPizzaSlicesLeft(totalSlices, totalBox))

    def testSmallPizzaSlicesLeft(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        totalSlices = PizzaApp.totalSlices(hungry, semiHungry, classic)
        totalBox = PizzaApp.recommendSmallSize(hungry, semiHungry, classic)
        self.assertEqual(0, PizzaApp.smallPizzaSlicesLeft(totalSlices, totalBox))

    def testAmountOfLargePizzaRecommended(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        totalBox = PizzaApp.recommendLargestSize(hungry,semiHungry,classic)
        self.assertEqual(10_000, PizzaApp.largePizzaAmountRecommended(totalBox))

    def testAmountOfMediumPizzaRecommended(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        totalBox = PizzaApp.recommendMediumSize(hungry,semiHungry,classic)
        self.assertEqual(12_000,PizzaApp.mediumPizzaAmountRecommended(totalBox))

    def testAmountOfSmallPizzaRecommended(self):
        hungry = 3
        semiHungry = 2
        classic = 4
        totalBox = PizzaApp.recommendSmallSize(hungry,semiHungry,classic)
        self.assertEqual(6_000, PizzaApp.smallPizzaAmountRecommended(totalBox))