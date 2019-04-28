package javaproj;

public class Ingredients {
    //------primary
    private static double flour;

    protected Ingredients(){
        flour = Admin.flour;
    }

    public static double getFlour() {
        return flour;
    }

    public static void setFlour(double flour) {
        Ingredients.flour -= flour;
    }


    //flour for cake
    //salt for cake
    //yeast for cake
    //puree for sauce
    //oil for sauce
    //salt for sauce
    //pepper for sauce
    //yellow cheese for cheese
    //------extended
}
