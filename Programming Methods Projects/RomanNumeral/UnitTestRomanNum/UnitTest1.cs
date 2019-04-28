using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using RomanNumeral;


namespace UnitTestRomanNum {
    [TestClass]
    public class GeneralTest {
        [TestMethod]
        public void fromRomanAssert() {
            Assert.AreEqual(Roman.fromRoman("I"), 1);
            Assert.AreEqual(Roman.fromRoman("II"), 2);
            Assert.AreEqual(Roman.fromRoman("III"), 3);
            Assert.AreEqual(Roman.fromRoman("IV"), 4);
            Assert.AreEqual(Roman.fromRoman("V"), 5);
            Assert.AreEqual(Roman.fromRoman("VI"), 6);
            Assert.AreEqual(Roman.fromRoman("VII"), 7);
            Assert.AreEqual(Roman.fromRoman("VIII"), 8);
            Assert.AreEqual(Roman.fromRoman("IX"), 9);
            Assert.AreEqual(Roman.fromRoman("X"), 10);
            Assert.AreEqual(Roman.fromRoman("L"), 50);
            Assert.AreEqual(Roman.fromRoman("C"), 100);
            Assert.AreEqual(Roman.fromRoman("D"), 500);
            Assert.AreEqual(Roman.fromRoman("M"), 1000);

            Assert.AreEqual(Roman.fromRoman("CXLVIII"), 148);
            Assert.AreEqual(Roman.fromRoman("DCCLXXXII"), 782);
            Assert.AreEqual(Roman.fromRoman("MDCCLIV"), 1754);
            Assert.AreEqual(Roman.fromRoman("MDCCCXXXII"), 1832);
            Assert.AreEqual(Roman.fromRoman("MMMDCCCXLIV"), 3844);
            Assert.AreEqual(Roman.fromRoman("MMMDCCCLXXXVIII"), 3888);
            Assert.AreEqual(Roman.fromRoman("MMMCMXCIX"), 3999);
            Assert.AreEqual(Roman.fromRoman("MMMMCMXCIX"), 4999);

        }

        [TestMethod]
        public void toRomanAssert() {

            Assert.AreEqual(Roman.toRoman(1), "I");
            Assert.AreEqual(Roman.toRoman(2), "II");
            Assert.AreEqual(Roman.toRoman(3), "III");
            Assert.AreEqual(Roman.toRoman(4), "IV");
            Assert.AreEqual(Roman.toRoman(5), "V");
            Assert.AreEqual(Roman.toRoman(6), "VI");
            Assert.AreEqual(Roman.toRoman(7), "VII");
            Assert.AreEqual(Roman.toRoman(8), "VIII");
            Assert.AreEqual(Roman.toRoman(9), "IX");
            Assert.AreEqual(Roman.toRoman(10), "X");
            Assert.AreEqual(Roman.toRoman(50), "L");
            Assert.AreEqual(Roman.toRoman(100), "C");
            Assert.AreEqual(Roman.toRoman(500), "D");
            Assert.AreEqual(Roman.toRoman(1000), "M");

            Assert.AreEqual(Roman.toRoman(148), "CXLVIII");
            Assert.AreEqual(Roman.toRoman(782), "DCCLXXXII");
            Assert.AreEqual(Roman.toRoman(1754), "MDCCLIV");
            Assert.AreEqual(Roman.toRoman(1832), "MDCCCXXXII");
            Assert.AreEqual(Roman.toRoman(3844), "MMMDCCCXLIV");
            Assert.AreEqual(Roman.toRoman(3888), "MMMDCCCLXXXVIII");
            Assert.AreEqual(Roman.toRoman(3999), "MMMCMXCIX");
            Assert.AreEqual(Roman.toRoman(4999), "MMMMCMXCIX");
        }
    }

    [TestClass]
    public class ComprehensiveTestToRoman {
        [TestMethod]
        public void caseCheck(){
            StringAssert.Contains("I", Roman.toRoman(1));
        }

        [TestMethod]
        public void emptyCheck(){
            Assert.IsNotNull(Roman.toRoman(1), "returned empty String");
        }

        [TestMethod]
        public void typeCheck(){
            Assert.IsInstanceOfType(Roman.toRoman(1), typeof(string), "Bad instance of return, should be String");
        }

    }

    [TestClass]
    public class ComprehensiveTestFromRoman{
        [TestMethod]
        public void emptyCheck(){
            Assert.IsNotNull(Roman.fromRoman("I"), "returned empty value");
        }

        [TestMethod]
        public void typeCheck(){
            Assert.IsInstanceOfType(Roman.fromRoman("I"), typeof(int), "Bad instance of return, should be Integer");
        }

        [TestMethod]
        public void upperBoundCheck(){
            Assert.IsFalse(Roman.fromRoman("") > 4999, "number is too big");
        } 

        [TestMethod]
        public void negativeZeroCheck(){
            Assert.IsFalse(Roman.fromRoman("") < 0, "negative numbers are rejected");
        }
    }

}
