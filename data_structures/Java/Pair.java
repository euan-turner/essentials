package Java;

public class Pair<Key,Value> {
    
    private Key key;
    private Value value;

    Pair(Key key, Value value) {
        this.key = key;
        this.value = value;
    }

    public Key getKey() {
        return key;
    }

    public Value getValue() {
        return value;
    }

    public static void main(String[] args) {
        Pair<Integer,Integer> pair = new Pair<>(1,10);
        System.out.println(pair.getKey());
        System.out.println(pair.getValue());

    }
}
