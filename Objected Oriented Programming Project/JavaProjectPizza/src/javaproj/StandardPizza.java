package javaproj;
import java.util.concurrent.TimeUnit;
import java.util.Scanner;

abstract class AbstractSmallPizza{
    public abstract void makingCake(Integer amount) throws InterruptedException;
    public abstract void preparingSauce(Integer amount) throws InterruptedException;
    public abstract void addingCheese(Integer amount) throws InterruptedException;
}

class SmallThinCrust extends AbstractSmallPizza{
    private double smallThinPrice = Values.getSmallThinPrice();
    protected double cost = smallThinPrice * GetAmount.GetAmount();

    SmallThinCrust(Integer amount){
        System.out.println("We are gonna make " + amount + " small thin crust pizzas");
    } // Implement the code here

    public void makingCake(Integer amount) throws InterruptedException{
        long duration = 5 * amount;
        System.out.println("We are making a Cake !");
        TimeUnit.SECONDS.sleep(duration);
        System.out.println("Cake finished !");
    }
    protected double useFlour(Integer amount){
        double flourAmount = 0.25;
        double flourDiff = flourAmount * amount;
        return flourDiff;
    }
    public void preparingSauce(Integer amount) throws InterruptedException{
        System.out.println("We are preparing a Sauce !");
        TimeUnit.SECONDS.sleep(5 * amount);
        System.out.println("Sauce finished !");
    }
    public void addingCheese(Integer amount)throws InterruptedException{
        System.out.println("We are adding a Cheese !");
        TimeUnit.SECONDS.sleep(5 * amount);
        System.out.println("Cheese added !");
    }
}
class SmallThickCrust extends AbstractSmallPizza{
    SmallThickCrust(String arg){
        System.out.println("Hello "+arg);
    } // Implement the code here
    public void makingCake() { };
    public void preparingSauce() { };
}

abstract class AbstractMediumPizza{
    //public abstract void operationB1();
    //public abstract void operationB2();
}

class MediumThinCrust extends AbstractMediumPizza{
    MediumThinCrust(String arg){
        System.out.println("Hello "+arg);
    } // Implement the code here
}

class MediumThickCrust extends AbstractMediumPizza{
    MediumThickCrust(String arg){
        System.out.println("Hello "+arg);
    } // Implement the code here
}

abstract class AbstractBigPizza{
    //public abstract void operationB1();
    //public abstract void operationB2();
}

class BigThinCrust extends AbstractBigPizza{
    BigThinCrust(String arg){
        System.out.println("Hello "+arg);
    } // Implement the code here
}

class BigThickCrust extends AbstractBigPizza{
    BigThickCrust(String arg){
        System.out.println("Hello "+arg);
    } // Implement the code here
}
abstract class AbstractFactory{
    abstract AbstractSmallPizza createSmallPizza(String cake,Integer amount);
    abstract AbstractMediumPizza createMediumPizza(String cake);
    abstract AbstractBigPizza createBigPizza(String cake);
}

class GdanskFactory extends AbstractFactory{
    AbstractSmallPizza createSmallPizza(String cake,Integer amount){
        String cakeFormated = String.format("%s", cake).toLowerCase();
        if (cakeFormated.equals("cienkie")){
            return new SmallThinCrust(amount);
        }
        else{
            return new SmallThickCrust("ProductA1");
        }
    }
    AbstractMediumPizza createMediumPizza(String cake){
        return new MediumThinCrust("ProductB1");
    }

    AbstractBigPizza createBigPizza(String cake){
        return new BigThickCrust("ProductB1");
    }
}

class GdyniaFactory extends AbstractFactory{
    AbstractSmallPizza createSmallPizza(){
        return new SmallThinCrust("ProductA1");
    }
    AbstractMediumPizza createMediumPizza(){
        return new MediumThinCrust("ProductB1");
    }

    AbstractBigPizza createBigPizza(){
        return new BigThickCrust("ProductB1");
    }
}

class SopotFactory extends AbstractFactory{
    AbstractSmallPizza createSmallPizza(){
        return new SmallThinCrust("ProductA1");
    }
    AbstractMediumPizza createMediumPizza(){
        return new MediumThinCrust("ProductB1");
    }

    AbstractBigPizza createBigPizza(){
        return new BigThickCrust("ProductB1");
    }
}

//Factory creator - an indirect way of instantiating the factories
class FactoryMaker{
    private static AbstractFactory location = null;
    static AbstractFactory getFactory(String choice){
        String choiceFormated = String.format("%s", choice).toLowerCase();
        switch (choice) {
            case "gdansk":
                location = new GdanskFactory();
                break;
            case "gdynia":
                location = new GdyniaFactory();
                break;
            case "sopot":
                location = new SopotFactory();
                break;
        }
        return location;
    }
}


// Client
public class StandardPizza{
    public static void main(String args[]) throws InterruptedException {
        Values price = new Values();
        Ingredients warehouse = new Ingredients();

        System.out.print(Admin.flour);
        Elements elements = new Elements();
        Client client = new Client(elements);
        elements.addObserver(client);
        client.updateFlour();
        client.delete();

        //ile pizz zamowic
        int amount = GetAmount.GetAmount();
        SmallThinCrust Pizza = new SmallThinCrust(amount);
        Values.setPrice(Pizza.cost);
        warehouse.setFlour(23);
        Pizza.makingCake(amount);
        Pizza.useFlour(23);
        AbstractFactory location=FactoryMaker.getFactory(String choice);
        AbstractSmallPizza product= location.createSmallPizza(String cake,Integer amount);
        //more function calls on product
    }
}