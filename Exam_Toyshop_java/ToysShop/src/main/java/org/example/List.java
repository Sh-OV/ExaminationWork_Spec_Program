package org.example;

import java.util.*;
import java.util.Arrays;
import java.util.Random;
import java.util.ArrayList;

public class List {
    public static int number = 10;
//    public static ArrayList<String> name = list_name();
 //   public static ArrayList<String> id = id_all();
    //public static HashMap<String, Toys> list_toys;
    public static ArrayList<Toys> list_toys;

    public static ArrayList<Toys> start() {
        for (int i = 0; i < number; i++) {
            list_toys.add(new Toys());
        }
        return list_toys;
    }
}
