from unittest import TestCase

from assignment import CreditCardValidatorServer


class Creditcard(TestCase):
    # def test_that_credit_cardValidatorExist(self):
    #     CreditCardValidatorServer creditCard = CreditCardValidatorServer
    #     self.assertIsNotNone(creditCard)

    def testThatCreditCardDigitsItUpTo13To16(self):
        digit = "4235678876432"
        self.assertEqual(len(digit),CreditCardValidatorServer.cardLength(digit))

    def testThatVisaCardsMustStartWith4(self):
        digit = "4235678876432"
        self.assertEqual(4,CreditCardValidatorServer.visaCardFirstDigit(digit))
