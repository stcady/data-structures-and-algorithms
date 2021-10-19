public interface BagInterface<T> {

    int getCurrentSize();

    boolean isEmpty();

    <T> boolean add(T item);

    <T> boolean remove(T item);

    void clear();

    int getFrequency(T item);

}


package com.example.lk2017;




import java.lang.reflect.Array;

import java.util.ArrayList;

import java.util.Comparator;

import java.util.Iterator;

import java.util.List;




public class Bag<T> implements BagInterface<T>, Comparator<T> {

    private static int BAG_CAPACITY = 10;

    List<T> items; // one-dimensional array using list to help generics

    private int lastIndex;




    // O(1)

    public int getCurrentSize() { return items.size(); }




    // O(1)

    public boolean isEmpty() { return (items.size() == 0); }




    // O(n) if each of the object needs to be null'ed

    // O(1) if the reference is null'ed

    public void clear() {}




    public int compare(T item, T newItem)

    {

       if (item.equals(newItem)) // will work for certain data types

           return 0;

        return -1;

    }




    public boolean remove (T item)

    {

        // locate the item, and replace the it with last item

        // call List remove method

        return true;

    }




    public void add (T item)

    {

        // Similar to Bag(item)

    }




    public int getFrequency(T item) {

        Iterator<T> iterator = items.iterator();

        int count = 0;

        while (iterator.hasNext()) {

            T nItem = iterator.next();

            if (compare(nItem, item) == 0)

            {

                count++;

            }

        }

        return count;

    }




    private Bag()  {

    }




    Bag(T item) {

        if (items != null) {

            if (items.size() == BAG_CAPACITY) {

                return; // rather silent

            } else {

                items = new ArrayList<T>();

            }

            items.add(item);

        }

    }




    Bag(T[] nItems) {

        if (items.size() == BAG_CAPACITY)

            return;

        if (items.size() + nItems.length > BAG_CAPACITY)

            // decisions decisions

            ;

        for (int i = 0; i < nItems.length; i++)

            items.add(nItems[i]);

    }

}



