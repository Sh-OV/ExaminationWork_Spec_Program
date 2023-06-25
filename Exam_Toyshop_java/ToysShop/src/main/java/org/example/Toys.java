package org.example;

import java.util.*;
import java.util.List;
import java.util.Random;

public class Toys {
    protected String        id;
    protected String        name;
    protected int           count_toy;
    protected int           weight;


    public Toys() {
        this.id = id_toy();
        this.name = name_toy();
        this.count_toy = rand_count();
        this.weight = lunges();
    }

    private static ArrayList<String> list_name() {
        ArrayList<String> list_toys = new ArrayList<>();
        for (int i = 0; i < Name_toy.values().length; i++){
            list_toys.add(String.valueOf(Name_toy.values()[i]));
        }
        return list_toys;
    }
    protected static String name_toy(){
        ArrayList<String> name_t = list_name();
        int index = new Random().nextInt(name_t.size());
        String name_rand = name_t.get(index);
        name_t.remove(index);
        return name_rand;
    }

    private static ArrayList<String> id_all() {
        ArrayList<String> id_all = new ArrayList<>();
        for (int i = 0; i < 1000; i++) {
            String k = String.valueOf(i);
            String num = k;
            if (k.length() < 6) {
                int n = 6 - k.length();
                while (n > 0) {
                    num = "0" + num;
                    n--;
                }
            }
            id_all.add(num);
        }
        return id_all;
    }
    protected static String id_toy(){
        ArrayList<String> id_t = id_all();
        int index = new Random().nextInt(id_t.size());
        String id_rand = id_t.get(index);
//        System.out.println(id);
//        System.out.println(id_rand);
        id_t.remove(index);
 //       System.out.println(id);
 //       System.out.println(id_rand);
        return id_rand;
    }

    private static int rand_count(){
        return new Random().nextInt(1,10);
    }

    private static int lunges(){
        List<Integer> lungesList = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8);
        Random rand = new Random();
        return lungesList.get(rand.nextInt(lungesList.size()));
    }

    public String toString() {
        return "id = " + id +
                "; name = " + name +
                "; count_toy = " + count_toy +
                "; weight = " + weight;
    }


}
