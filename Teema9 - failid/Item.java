import java.util.Arrays;


public class Item implements Comparable {

    public final int value;

    public Item(int value) {
        this.value = value;
    }

    @Override
    public int compareTo(Object o) {

        int other = 0;
        if (o.getClass() == Item.class) {
            other = ((Item) o).value;
        }

        if (o.getClass() == Item2.class) {
            other = ((Item2) o).value;
        }

        if (value < other)  {
            return  -10;
        } else {
            return 1;
        }

//        return Integer.compare(value, other);
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

    public static void main(String[] args) {
        Object[] arr = {new Item(4), new Item2(2), new Item2(3)};

        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
