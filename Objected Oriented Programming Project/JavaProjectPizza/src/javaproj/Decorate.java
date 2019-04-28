package javaproj;
import java.util.concurrent.TimeUnit;

abstract class AbstractProduct {

    public void makeDecorate(Integer amount) throws InterruptedException { }

    public abstract double price(Integer amount);

    @Override
    public String toString() {
        return price() + "(" + makeDecorate() + ")";
    }
}
class PizzaDecorate extends AbstractProduct {

    public String PizzaDecorate(SmallThinCrust pizza) {
        return  "We are gonna make decorations now";
    }


    public double price(Integer amount) {
        return Values.getPrice();
    }

}
abstract class AbstractProductDecorator extends AbstractProduct {
    protected AbstractProduct product;

    public AbstractProductDecorator(AbstractProduct product) {
            this.product = product;
    }


    public abstract void makeDecorate(Integer amount) throws InterruptedException;

    public abstract double price(Integer amount);
}

class Ham extends AbstractProductDecorator {
    protected double hamPrice = Ingredients.getFlour();

    public Ham(AbstractProduct product) {
        super(product);
    }

    @Override
    public void makeDecorate(Integer amount) throws InterruptedException {
        System.out.println("We are adding Ham !");
        TimeUnit.SECONDS.sleep(2 * amount);
        System.out.println("Ham added !");
    }
    protected double useHam(Integer amount){
        double hamAmount = 0.25;
        double hamDiff = hamAmount * amount;
        return hamDiff;
    }

    public double price(Integer amount) {
        return hamPrice * amount;
    }

}

class OlivesDecorator extends AbstractProductDecorator {

    public OlivesDecorator(AbstractProduct product) {
        super(product);
    }

    @Override
    public void makeDecorate() {
        return product.makeDecorate() + ", oliwki";
    }

    @Override
    public double price() {
        return product.price() + 2.50;
    }

}

class ParmaHamDecorator extends AbstractProductDecorator {

    public ParmaHamDecorator(AbstractProduct product) {
        super(product);
    }

    @Override
    public void makeDecorate() {
        return product.makeDecorate() + ", szynka parmeńska";
    }

    @Override
    public double price() {
        return product.price() + 5.25;
    }

}

public class Decorate {
    public void main(String args[]) throws InterruptedException{
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
        SmallThinCrust pizza = new SmallThinCrust(amount);
        Values.setPrice(pizza.cost);
        warehouse.setFlour(23);
        pizza.makingCake(amount);
        double asd = pizza.useFlour(23);
        Ingredients.setFlour(asd);
        Admin.flour = client.updateFlour();
        AbstractProduct pizzaDecorate;

//Pizza z podwójnym serem, szynką parmeńską i oliwkami
        pizzaDecorate = new PizzaDecorate();

        pizzaDecorate = new Ham(pizzaDecorate);
        Ham ham = new Ham(pizzaDecorate);
        ham.useHam(54);
        Values.setPrice(ham.hamPrice);

        pizzaDecorate = new ParmaHamDecorator(pizzaDecorate);
        pizzaDecorate = new OlivesDecorator(pizzaDecorate);
    }
}
