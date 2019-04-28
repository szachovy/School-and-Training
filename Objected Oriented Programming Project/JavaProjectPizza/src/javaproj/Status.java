package javaproj;

import java.util.*;


interface Observed {
    public void addObserver(Client observer);
    public void delObserver(Client observer);
}


interface Raport {

    /* publikuje wyniki losowania */
    public void inform();
}

class Admin {
    protected static double flour = 23;
}

/* oberwowany obiekt */
class Elements extends Ingredients implements Observed {
    private ArrayList<Observer> observers;

    public Elements(){
        observers = new ArrayList<Observer>();
    }

    public void addObserver(Client observer){
        observers.add((Observer) observer);
    }

    public void delObserver(Client observer){
        int index = observers.indexOf(observer);
        observers.remove(index);
    }

    public double putonFlour(double flour){
        Admin.flour = flour;
        return Admin.flour;
    }
}//class


/* obserwator */
class Client extends Ingredients implements Raport {
    private Elements usage;

    public Client(Elements usage){
        this.usage = usage;
    }

    public static double updateFlour(){
        Admin.flour = Ingredients.getFlour();
        return Admin.flour;
    }

    public void inform(){
        System.out.println("Amount of flour is equal" + Admin.flour);

    }

    public void delete(){
        usage.delObserver(this);
    }
}