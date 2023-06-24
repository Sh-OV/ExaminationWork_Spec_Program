package org.example;
import javax.swing.*;
import java.util.ArrayList;

public class Panel {
        public static void main(String args[]) {
            JFrame a = new JFrame("Toys Shop");
            JTextField b = new JTextField("edureka");
            ArrayList<Toys> aList = List.list_toys;

            DefaultListModel<String> model = new DefaultListModel<String>();
            for(Toys s:aList){
                model.addElement(String.valueOf(s));
            }
            JList<String> nameList = new JList<String>(model); 

            nameList.setBounds(100,100,75,75);
            b.setBounds(50,100,200,30);
            a.add(b);
            a.setSize(600,800);
            a.setLayout(null);
            a.setVisible(true);
        }

}
