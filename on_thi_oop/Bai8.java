package kiemtra01;
import java.io.*;
import java.util.*;
public class Bai8 {
    public static void main(String[] args) throws IOException {
        try (Scanner sc = new Scanner(System.in)) {
            int n = Integer.parseInt(sc.nextLine());
            ArrayList<HoaDon> ds = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String maMatHang = sc.nextLine();
                String tenMatHang = sc.nextLine();
                int soLuong = Integer.parseInt(sc.nextLine());
                long donGia = Long.parseLong(sc.nextLine());
                long chietKhau = Long.parseLong(sc.nextLine());
                ds.add(new HoaDon(maMatHang, tenMatHang, soLuong, donGia, chietKhau));
            }
            Collections.sort(ds);
            for (HoaDon hd : ds) {
                System.out.println(hd);
            }
        }
    }
}

class HoaDon implements Comparable<HoaDon> {
    private String maMatHang;
    private String tenMatHang;
    private int soLuong;
    private long donGia;
    private long chietKhau;
    private long tongTien;
    
    public HoaDon(String maMatHang, String tenMatHang, int soLuong, long donGia, long chietKhau) {
        this.maMatHang = maMatHang;
        this.tenMatHang = tenMatHang;
        this.soLuong = soLuong;
        this.donGia = donGia;
        this.chietKhau = chietKhau;
        this.tongTien = donGia * soLuong - chietKhau;
    }
    
    @Override
    public String toString() {
        return maMatHang + " " + tenMatHang + " " + soLuong + " " + donGia + " " + chietKhau + " " + tongTien;
    }
    
    @Override
    public int compareTo(HoaDon o) {
        // Sắp xếp theo tổng tiền giảm dần
        return Long.compare(o.tongTien, this.tongTien);
    }
}
