package kiemtra01;
import java.io.*;
import java.util.*;
public class Bai7 {
    public static void main(String[] args) throws IOException {
        try (Scanner sc = new Scanner(System.in)) {
            int n = Integer.parseInt(sc.nextLine());
            ArrayList<MonHoc> ds = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String maMon = sc.nextLine();
                String tenMon = sc.nextLine();
                String hinhThucThi = sc.nextLine();
                ds.add(new MonHoc(maMon, tenMon, hinhThucThi));
            }
            Collections.sort(ds);
            for (MonHoc mh : ds) {
                System.out.println(mh);
            }
        }
    }
}

class MonHoc implements Comparable<MonHoc> {
    private String maMon;
    private String tenMon;
    private String hinhThucThi;
    
    public MonHoc(String maMon, String tenMon, String hinhThucThi) {
        this.maMon = maMon;
        this.tenMon = tenMon;
        this.hinhThucThi = hinhThucThi;
    }
    
    @Override
    public String toString() {
        return maMon + " " + tenMon + " " + hinhThucThi;
    }
    
    @Override
    public int compareTo(MonHoc o) {
        // Sắp xếp theo mã môn theo thứ tự từ điển
        return this.maMon.compareTo(o.maMon);
    }
}
