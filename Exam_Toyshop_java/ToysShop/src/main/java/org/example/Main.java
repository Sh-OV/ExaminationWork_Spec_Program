package org.example;

import java.util.ArrayList;
import java.util.Random;

public class Main {
    protected static int number = 10;
    protected static ArrayList<Toys> list_toys = start();

    public static void main(String[] args) {
        //List.name_toys();
        //List.id_toys();
        System.out.println(Toys.name_toy());
        System.out.println("\n------Перечень игрушек для призов:------");
        list_toys.forEach(n -> System.out.println(n.toString()));
        work(winning());
        list_toys.forEach(n -> System.out.println(n.toString()));
        //GIU.panel();

    }

    protected static ArrayList<Toys> start() {
        ArrayList<Toys> lt = new ArrayList<>();
        for (int i = 0; i < number; i++) {
            Toys toy = new Toys();
            lt.add(toy);
        }
        return lt;
    }

    protected static Toys winning(){
        int index = new Random().nextInt(list_toys.size());
        Toys win_toy = list_toys.get(index);
        System.out.println("win_toy = " + win_toy);
        return win_toy;
    }
    public static void work(Toys toy){
        for (Toys winn : list_toys) {
            if (winn.id == toy.id) {
                if (winn.count_toy < 1){
                    list_toys.remove(winn);
                }
                else  winn.count_toy -= 1;
            }
        }
    }
}
