public class Item2 implements Comparable {

    public final int value;

    public Item2(int value) {
        this.value = value;
    }

    @Override
    public int compareTo(Object o) {
//        return 0;
//
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
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}
