package org.example;

import java.util.ArrayList;
import java.util.Random;
import java.io.*;
import java.io.FileWriter;
public class Main {
    protected static int number = 10;
    protected static ArrayList<Toys> list_toys = start();

    public static void main(String[] args) throws IOException {
        System.out.println("\n------Перечень игрушек для призов:------");
        list_toys.forEach(n -> System.out.println(n.toString()));
        write_txt();
        work(winning());
        list_toys.forEach(n -> System.out.println(n.toString()));
        write_txt();
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
        ArrayList<Integer> ver = new ArrayList<>();
        for (Toys win : list_toys) {
            for (int i = 0; i < win.weight; i++) {
                ver.add(win.weight);
            }
        }
        System.out.println(ver);
        Toys win_toy = null;
        int index = new Random().nextInt(ver.size());
        System.out.println("ver.size() = " + ver.size());
        int w = ver.get(index);
        //System.out.println("w = " + w);
        int i = 0;
        for (Toys win : list_toys) {
            if (win.weight == w){
                //System.out.println("win.weight = " + win.weight);
                //System.out.println("i = " + i);
                win_toy = list_toys.get(i);
                System.out.println("\n------Выигрыш - игрушка: " + win_toy + "------\n");
                break;
            }
            i++;
        }
        return win_toy;
    }
    public static void work(Toys toy){
        int d = 0;
        int i = 0;
        int x = -1;
        for (Toys winn : list_toys) {
            if (winn.id == toy.id) {
                if (winn.count_toy > 1){
                    winn.count_toy -= 1;
                }
                else {
                    x = i;
                    d = 1;
                }
            }
            i++;
        }
        if (d == 1){
            list_toys.remove(x);
        }
    }

    public static void write_txt() throws IOException {
        FileWriter writer = new FileWriter("ListToys.txt");
        for(Toys str: list_toys) {
            writer.write(str + System.lineSeparator());
        }
        writer.close();
    }
}

