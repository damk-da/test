package kiemtra01;
import java.io.*;
import java.util.*;
public class Bai6 {
    public static void main(String[] args) throws IOException {
        try (Scanner sc = new Scanner(new File("LUYENTAP.in"))) {
            int n = Integer.parseInt(sc.nextLine());
            ArrayList<SinhVien> ds = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String hoTen = sc.nextLine();
                String line = sc.nextLine();
                String[] parts = line.split(" ");
                int soBaiDung = Integer.parseInt(parts[0]);
                int tongSubmit = Integer.parseInt(parts[1]);
                ds.add(new SinhVien(hoTen, soBaiDung, tongSubmit));
            }
            Collections.sort(ds);
            for (SinhVien sv: ds){
                System.out.println(sv);
            }
        }
    }
}
class SinhVien implements Comparable<SinhVien> {
    private String hoTen;
    private int soBaiDung;
    private int tongSubmit;
    
    public SinhVien(String hoTen, int soBaiDung, int tongSubmit) {
        this.hoTen = hoTen;
        this.soBaiDung = soBaiDung;
        this.tongSubmit = tongSubmit;
    }
    
    @Override
    public String toString() {
        return hoTen + " " + soBaiDung + " " + tongSubmit;
    }
    
    @Override
    public int compareTo(SinhVien o) {
        // Sắp xếp theo số bài làm đúng (nhiều hơn xếp trước)
        if (this.soBaiDung != o.soBaiDung) {
            return Integer.compare(o.soBaiDung, this.soBaiDung); // Descending
        }
        // Nếu cùng số bài làm đúng, ưu tiên sinh viên có số lượt submit ít hơn
        if (this.tongSubmit != o.tongSubmit) {
            return Integer.compare(this.tongSubmit, o.tongSubmit); // Ascending
        }
        // Nếu cùng hạng, sắp xếp theo họ tên theo thứ tự từ điển
        return this.hoTen.compareTo(o.hoTen);
    }
}

