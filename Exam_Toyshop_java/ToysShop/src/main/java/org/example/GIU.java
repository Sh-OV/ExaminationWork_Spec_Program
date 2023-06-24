package org.example;

import javax.swing.*;
import java.util.ArrayList;
import javax.swing.*;
import java.util.ArrayList;
public class GIU {

    protected static JFrame a = new JFrame("Toys Shop");
    protected static JTextField b = new JTextField("edureka");
    //protected static ArrayList<String> aList = List.name;
    protected static ArrayList<String> aList = new ArrayList<>();

    protected static DefaultListModel<String> model = new DefaultListModel<String>();

    public static void panel () {
        for (String s : aList) {
            model.addElement(s);
        }
        JList<String> nameList = new JList<String>(model);

        nameList.setBounds(100, 100, 75, 75);
        b.setBounds(50, 100, 200, 30);
        a.add(b);
        a.setSize(600, 800);
        a.setLayout(null);
        a.setVisible(true);
    }

}
