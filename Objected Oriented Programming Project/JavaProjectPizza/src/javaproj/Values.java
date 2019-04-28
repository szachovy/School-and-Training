package javaproj;

public class Values{
    //price
    private static double price;

    protected Values() {
        price = 0;
    }

    public static double getPrice() {
        return price;
    }

    public static void setPrice(double price) {
        Values.price += price;
    }
    private static double SmallThinPrice = 25;

    public static double getSmallThinPrice() {
        return SmallThinPrice;
    }

    public void setSmallThinPrice(double smallThinPrice) {
        SmallThinPrice = smallThinPrice;
    }

}
