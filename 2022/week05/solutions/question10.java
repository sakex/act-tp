import java.util.List;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) {
        var ma_liste = List.of(1,2,3,4);
        System.out.println(ma_liste.get(1));
        System.out.println(ma_liste.size());
        var ma_liste_m = new LinkedList<>(ma_liste);
        ma_liste_m.addFirst(0);
        ma_liste_m.addLast(6);
        for(int i=0;i<ma_liste_m.size();i++){
            System.out.println(ma_liste_m.get(i));
        }
    }
}
