package javaproj;
import java.util.Scanner;

class Kind{
    int PizzaKind(){
        System.out.println("On small size thin crust SELECT --> 1");
        System.out.println("On small size thick crust SELECT --> 2");
        System.out.println("On medium size thin crust SELECT --> 3");
        System.out.println("On medium size thick crust SELECT --> 4");
        System.out.println("On big size thin crust SELECT --> 5");
        System.out.println("On big size thick crust SELECT --> 6");
        int choose;
        Scanner in = new Scanner(System.in);
        choose = in.nextInt();

        while (choose != 1 || choose != 2 || choose != 3 || choose != 4 || choose != 5 || choose != 6){
            System.out.println("Wrong choose try again !");
            choose = in.nextInt();
        }
        return choose;
    }
}
class Amount{
    int GetAmount(){
        int amount;
        Scanner in = new Scanner(System.in);
        amount = in.nextInt();
        while (amount <= 0){
            System.out.println("Wrong number try again !");
            amount = in.nextInt();
        }
        return amount;
    }
}
class IngredientsOnPizza{
    boolean GetHamOnPizza(){
        boolean GetHamOnPizza;
        Scanner reader = new Scanner(System.in);
        char getInput = reader.findInLine(".").charAt(0);
        getInput = Character.toUpperCase(getInput);
        switch (getInput){
            case 'T':
                GetHamOnPizza = true;
                return GetHamOnPizza;
            case 'N':
                GetHamOnPizza = false;
                return GetHamOnPizza;
            default:
                System.out.print("Error with typing try again ! ");
                return GetHamOnPizza();
        }
    }
    boolean GetMushroomsOnPizza(){
        boolean GetMushroomsOnPizza;
        Scanner reader = new Scanner(System.in);
        char getInput = reader.findInLine(".").charAt(0);
        getInput = Character.toUpperCase(getInput);
        switch (getInput){
            case 'T':
                GetMushroomsOnPizza = true;
                return GetMushroomsOnPizza;
            case 'N':
                GetMushroomsOnPizza = false;
                return GetMushroomsOnPizza;
            default:
                System.out.println("Error with typing try again !");
                return GetMushroomsOnPizza();
        }
}
public class Main {
    public void main(String[] args) throws InterruptedException {
    System.out.println("You are in queue");

    System.out.println("What kind of pizza would you like to order");
    int chosen = new Kind().PizzaKind();

    System.out.print("How much pizzas do you want to order ? ->");
    int amount = new Amount().GetAmount();

    //tu beda gotowe wzory pizz do zamowienia

    System.out.print("Do you want to get Ham on your pizza :[T/N] ");
    boolean getHamOnPizza = new IngredientsOnPizza().GetHamOnPizza();

    System.out.print("Do you want to get Mushrooms on your pizza :[T/N] ");
    boolean getMushroomsOnPizza = new IngredientsOnPizza().GetMushroomsOnPizza();



    }
}
