# ============================================================================
# PYTHON EXAM CHEAT SHEET - ĐỀ CƯƠNG ÔN TẬP
# ============================================================================

# ============================================================================
# BÀI 1: BIẾN, STRING, LOGIC CƠ BẢN
# ============================================================================

# --- NHẬP INPUT CƠ BẢN ---
def input_basic():
    # Nhập số nguyên
    n = int(input())
    
    # Nhập số thực
    x = float(input())
    
    # Nhập chuỗi
    s = input()
    
    # Nhập nhiều số trên một dòng
    a, b, c = map(int, input().split())
    
    # Nhập list số nguyên
    numbers = list(map(int, input().split()))


# --- VÒNG LẶP VỚI SỐ BỘ TEST ---
def bai1_gia_ve_cong_vien():
    """
    Tính giá vé vào công viên theo độ tuổi
    <4 tuổi: FREE
    4-18 tuổi: 10
    18-60 tuổi: 20
    >60 tuổi: 15
    """
    count = int(input())
    for _ in range(count):
        age = int(input())
        if age < 4:
            print('FREE')
        elif age < 18:
            print(10)
        elif age < 60:
            print(20)
        else:
            print(15)


# --- XỬ LÝ CHUỖI CƠ BẢN ---
def string_operations():
    # Kiểm tra ký tự
    c = 'a'
    if c.isalpha():      # Chữ cái
        print("Là chữ cái")
    if c.isdigit():      # Chữ số
        print("Là số")
    if c.isupper():      # Chữ hoa
        print("Chữ hoa")
    if c.islower():      # Chữ thường
        print("Chữ thường")
    
    # Xử lý chuỗi
    s = "  Hello World  "
    s.strip()    # Xóa khoảng trắng đầu/cuối
    s.lower()    # Chuyển thường
    s.upper()    # Chuyển hoa
    s.split()    # Tách thành list
    
    # Join list thành chuỗi
    words = ['hello', 'world']
    result = " ".join(words)  # "hello world"


# --- CẤU TRÚC IF-ELIF-ELSE ---
def if_else_example():
    x = int(input())
    
    if x > 0:
        print("Dương")
    elif x < 0:
        print("Âm")
    else:
        print("Bằng 0")


# --- VÒNG LẶP FOR ---
def loop_examples():
    # Lặp với range
    for i in range(5):        # 0, 1, 2, 3, 4
        print(i)
    
    for i in range(1, 6):     # 1, 2, 3, 4, 5
        print(i)
    
    for i in range(0, 10, 2): # 0, 2, 4, 6, 8
        print(i)
    
    # Lặp qua list
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)
    
    # Lặp với index
    for i in range(len(numbers)):
        print(f"Index {i}: {numbers[i]}")


# ============================================================================
# BÀI 2: THAO TÁC VỚI LIST
# ============================================================================

# --- XỬ LÝ CHUỖI VÀ LỌC KÝ TỰ ---
def bai2_xu_ly_chuoi():
    """
    Đếm độ dài các từ sau khi loại bỏ ký tự không phải chữ cái
    """
    n = int(input())
    for _ in range(n):
        s = input().split()  # Tách thành list các từ
        result = []
        
        for word in s:
            # Lọc chỉ giữ chữ cái
            clean_word = ''.join(c for c in word if c.isalpha())
            
            if len(clean_word) > 0:
                result.append(str(len(clean_word)))
        
        print(" ".join(result))


# --- LIST COMPREHENSION ---
def list_comprehension_examples():
    # Tạo list số chẵn từ 0-10
    even_numbers = [x for x in range(11) if x % 2 == 0]
    
    # Chuyển list string thành list int
    numbers = [int(x) for x in input().split()]
    
    # Lọc các phần tử thỏa điều kiện
    filtered = [x for x in numbers if x > 10]
    
    # Bình phương các số
    squares = [x**2 for x in range(10)]
    
    # Lọc và transform
    result = [x*2 for x in numbers if x % 2 == 0]


# --- CÁC THAO TÁC LIST PHỔ BIẾN ---
def list_operations():
    lst = [3, 1, 4, 1, 5]
    
    # Thêm phần tử
    lst.append(9)           # Thêm vào cuối
    lst.insert(0, 2)        # Chèn vào vị trí 0
    lst.extend([2, 6])      # Thêm nhiều phần tử
    
    # Xóa phần tử
    lst.remove(1)           # Xóa phần tử có giá trị 1 (đầu tiên)
    lst.pop()               # Xóa và trả về phần tử cuối
    lst.pop(0)              # Xóa và trả về phần tử ở vị trí 0
    
    # Sắp xếp
    lst.sort()              # Tăng dần (thay đổi list gốc)
    lst.sort(reverse=True)  # Giảm dần
    sorted_lst = sorted(lst) # Trả về list mới đã sắp xếp
    
    # Đảo ngược
    lst.reverse()
    
    # Tìm kiếm
    if 4 in lst:
        print("Tìm thấy")
        index = lst.index(4)  # Tìm vị trí đầu tiên
    
    # Đếm
    count = lst.count(1)    # Đếm số lần xuất hiện
    
    # Độ dài
    length = len(lst)
    
    # Min, Max, Sum
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    
    # Slicing
    sub_list = lst[1:4]     # Lấy phần tử từ index 1 đến 3
    first_three = lst[:3]   # 3 phần tử đầu
    last_three = lst[-3:]   # 3 phần tử cuối


# ============================================================================
# BÀI 3: THAO TÁC VỚI DICTIONARY
# ============================================================================

# --- TẠO VÀ THAO TÁC DICTIONARY CƠ BẢN ---
def dictionary_basics():
    # Tạo dictionary rỗng
    dict1 = {}
    dict2 = dict()
    
    # Tạo dictionary với dữ liệu
    dict3 = {'name': 'John', 'age': 25, 'city': 'Hanoi'}
    
    # Thêm/cập nhật phần tử
    dict1['hello'] = 'xin chào'
    dict1['cat'] = 'con mèo'
    
    # Truy xuất phần tử
    value = dict1['hello']                    # Lỗi nếu key không tồn tại
    value = dict1.get('hello')                # Trả về None nếu không tồn tại
    value = dict1.get('dog', 'Not found')     # Trả về giá trị mặc định
    
    # Kiểm tra key có tồn tại
    if 'hello' in dict1:
        print("Tồn tại")
    
    # Xóa phần tử
    del dict1['hello']
    value = dict1.pop('cat')  # Xóa và trả về giá trị
    
    # Lấy tất cả keys, values, items
    keys = dict1.keys()
    values = dict1.values()
    items = dict1.items()  # List của (key, value) tuples
    
    # Duyệt qua dictionary
    for key in dict1:
        print(f"{key}: {dict1[key]}")
    
    for key, value in dict1.items():
        print(f"{key}: {value}")


# --- BÀI TỪ ĐIỂN SONG NGỮ ---
def bai3_tu_dien_song_ngu():
    """
    Xây dựng từ điển Anh-Việt với hai lệnh:
    - add eng viet: Thêm/cập nhật từ
    - find eng: Tra cứu từ
    """
    count = int(input())
    dict1 = {}
    
    for _ in range(count):
        s = input().split()
        
        if s[0] == 'add':
            key = s[1]
            # Lấy tất cả các từ từ vị trí 2 trở đi
            list_value = [s[i] for i in range(2, len(s))]
            value = " ".join(list_value)
            dict1[key] = value
        
        elif s[0] == 'find':
            print(dict1.get(s[1], 'Not found'))


# --- DICTIONARY NÂNG CAO ---
def dictionary_advanced():
    # Nested dictionary
    students = {
        'SV001': {'name': 'Nguyen Van A', 'score': 8.5},
        'SV002': {'name': 'Tran Thi B', 'score': 9.0}
    }
    
    # Truy xuất nested
    name = students['SV001']['name']
    
    # Dictionary comprehension
    squares = {x: x**2 for x in range(5)}
    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    
    # Lọc dictionary
    high_scores = {k: v for k, v in students.items() 
                   if v['score'] >= 9.0}


# ============================================================================
# BÀI 4: CLASS, OBJECT, LIST OF OBJECT
# ============================================================================

# --- ĐỊNH NGHĨA CLASS ---
class Student:
    """Class sinh viên với các thuộc tính và phương thức"""
    
    def __init__(self, id, name, toan, ly, hoa, course, lop):
        """Constructor - Khởi tạo đối tượng"""
        self.id = id
        self.name = name
        self.toan = float(toan)
        self.ly = float(ly)
        self.hoa = float(hoa)
        self.course = int(course)
        self.lop = lop
        self.total = self.toan + self.ly + self.hoa
    
    def __str__(self):
        """Phương thức in đối tượng"""
        return f"{self.id} {self.name} {self.total:.2f} {self.lop} {self.course}"
    
    def calculate_average(self):
        """Phương thức tính điểm trung bình"""
        return self.total / 3


# --- VÍ DỤ CLASS KHÁC ---
class Worker:
    """Class công nhân"""
    
    def __init__(self, id, name, salary, years):
        self.id = id
        self.name = name
        self.salary = float(salary)
        self.years = int(years)  # Số năm làm việc (thâm niên)
    
    def __str__(self):
        return f"{self.id} {self.name} {self.salary:.2f} {self.years}"


class Product:
    """Class sản phẩm"""
    
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
    
    def total_value(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.id} {self.name} {self.price:.2f} {self.quantity}"


# --- ĐỌC DỮ LIỆU VÀ TẠO LIST OF OBJECTS ---
def bai4_quan_ly_sinh_vien():
    """
    Quản lý danh sách sinh viên, sắp xếp theo tổng điểm
    """
    T = int(input().strip())
    
    for t in range(1, T + 1):
        n = int(input().strip())
        students = []
        
        for _ in range(n):
            parts = input().strip().split()
            
            # Lấy các trường từ cuối
            id = parts[0]
            toan = parts[-5]
            ly = parts[-4]
            hoa = parts[-3]
            course = parts[-2]
            lop = parts[-1]
            
            # Tên có thể chứa khoảng trắng
            name = " ".join(parts[1:-5])
            
            students.append(Student(id, name, toan, ly, hoa, course, lop))
        
        # Sắp xếp giảm dần theo total, nếu bằng thì tăng dần theo id
        students.sort(key=lambda x: (-x.total, x.id))
        
        print(f"Case #{t}:")
        for s in students:
            print(s)


# --- SẮP XẾP LIST OF OBJECTS VỚI LAMBDA ---
def sorting_examples():
    students = []  # Giả sử đã có dữ liệu
    
    # Sắp xếp giảm dần theo total, nếu bằng thì tăng dần theo id
    students.sort(key=lambda x: (-x.total, x.id))
    
    # Sắp xếp tăng dần theo tên
    students.sort(key=lambda x: x.name)
    
    # Sắp xếp theo nhiều tiêu chí
    students.sort(key=lambda x: (-x.total, x.course, x.id))
    
    # Sắp xếp công nhân theo thâm niên (giảm dần)
    workers = []  # Giả sử đã có dữ liệu
    workers.sort(key=lambda x: -x.years)
    
    # Sắp xếp sản phẩm theo số lượng bán (giảm dần)
    products = []  # Giả sử đã có dữ liệu
    products.sort(key=lambda x: -x.quantity)
    
    # Dùng sorted() để tạo list mới
    sorted_students = sorted(students, key=lambda x: -x.total)


# ============================================================================
# BÀI 5: ĐỌC FILE JSON VÀ CSV
# ============================================================================

# --- ĐỌC FILE JSON ---
def bai5_doc_file_json():
    """
    Đọc file JSON và tính thống kê về total_bill
    """
    import json
    
    # Đọc file JSON
    with open('tips.json', encoding='utf-8') as f:
        du_lieu = json.load(f)
    
    # Nếu JSON có nested structure
    tips = du_lieu['tips']  # Lấy list tips
    
    # Xử lý queries
    n = int(input())
    for _ in range(n):
        dong = input().strip().split()
        gioi_tinh = dong[0]  # Male/Female
        hut_thuoc = dong[1]   # Yes/No
        
        # Lọc các item phù hợp
        item_phu_hop = []
        for item in tips:
            if item['sex'] == gioi_tinh and item['smoker'] == hut_thuoc:
                item_phu_hop.append(float(item['total_bill']))
        
        # Tính toán thống kê
        if item_phu_hop:
            tong = sum(item_phu_hop)
            tb = tong / len(item_phu_hop)
            lon_nhat = max(item_phu_hop)
            nho_nhat = min(item_phu_hop)
            print(f"{tong:.4f} {tb:.4f} {lon_nhat:.4f} {nho_nhat:.4f}")
        else:
            print("0.0000 0.0000 0.0000 0.0000")


# --- VÍ DỤ JSON KHÁC ---
def json_examples():
    import json
    
    # Đọc file JSON
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
    
    # Ghi file JSON
    data_to_write = {'name': 'John', 'age': 25}
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_write, f, ensure_ascii=False, indent=2)
    
    # Parse JSON string
    json_string = '{"name": "John", "age": 25}'
    data = json.loads(json_string)
    
    # Convert to JSON string
    json_string = json.dumps(data, ensure_ascii=False)


# --- ĐỌC FILE CSV ---
def csv_examples():
    import csv
    
    # Đọc file CSV với DictReader
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            name = row['name']
            age = int(row['age'])
            score = float(row['score'])
            print(f"{name}: {age} tuổi, điểm: {score}")
    
    # Đọc file CSV với reader thường
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Dòng đầu tiên
        
        for row in reader:
            print(row)  # row là list


# --- ĐỌC CSV THỦ CÔNG (KHÔNG DÙNG THƯ VIỆN) ---
def csv_manual():
    with open('data.csv', encoding='utf-8') as f:
        lines = f.readlines()
        
        # Dòng đầu là header
        header = lines[0].strip().split(',')
        
        # Các dòng còn lại là dữ liệu
        for line in lines[1:]:
            values = line.strip().split(',')
            # Xử lý dữ liệu
            print(values)


# --- ĐỌC FILE TEXT THÔNG THƯỜNG ---
def read_text_file():
    # Đọc toàn bộ file
    with open('data.txt', encoding='utf-8') as f:
        content = f.read()
    
    # Đọc từng dòng vào list
    with open('data.txt', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Đọc từng dòng (tiết kiệm bộ nhớ)
    with open('data.txt', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # Xóa ký tự xuống dòng
            print(line)


# ============================================================================
# TEMPLATE TỔNG HỢP
# ============================================================================

# --- TEMPLATE CHUNG CHO BÀI THI ---
def template_bai_thi():
    """
    Template chuẩn cho bài thi có nhiều test case
    """
    T = int(input().strip())
    
    for t in range(1, T + 1):
        # Đọc input
        n = int(input().strip())
        
        # Xử lý logic ở đây
        result = []
        for _ in range(n):
            # Đọc và xử lý từng dòng
            data = input().strip()
            # ... xử lý ...
        
        # In kết quả
        print(f"Case #{t}:")
        for item in result:
            print(item)


# --- TEMPLATE CHO BÀI LIST OF OBJECTS ---
def template_list_of_objects():
    """
    Template cho bài quản lý danh sách đối tượng
    """
    # Định nghĩa class (đặt ở đầu file)
    class Item:
        def __init__(self, id, name, value):
            self.id = id
            self.name = name
            self.value = float(value)
        
        def __str__(self):
            return f"{self.id} {self.name} {self.value:.2f}"
    
    # Main logic
    n = int(input())
    items = []
    
    # Đọc dữ liệu
    for _ in range(n):
        parts = input().split()
        # Xử lý parts và tạo object
        item = Item(parts[0], parts[1], parts[2])
        items.append(item)
    
    # Sắp xếp
    items.sort(key=lambda x: -x.value)
    
    # In kết quả
    for item in items:
        print(item)


# ============================================================================
# HÀM HỮU ÍCH
# ============================================================================

def useful_functions():
    # Format số thập phân
    x = 3.14159
    print(f"{x:.2f}")   # 3.14
    print(f"{x:.4f}")   # 3.1416
    
    # Làm tròn
    print(round(x, 2))  # 3.14
    
    # Giá trị tuyệt đối
    print(abs(-5))      # 5
    
    # Lũy thừa
    print(pow(2, 3))    # 8
    print(2 ** 3)       # 8
    
    # Chia lấy nguyên và chia lấy dư
    print(7 // 2)       # 3
    print(7 % 2)        # 1
    
    # Min, max của nhiều số
    print(min(1, 5, 3)) # 1
    print(max(1, 5, 3)) # 5
    
    # Kiểm tra kiểu dữ liệu
    x = 5
    print(type(x))              # <class 'int'>
    print(isinstance(x, int))   # True


# --- XỬ LÝ NGOẠI LỆ ---
def exception_handling():
    try:
        x = int(input())
        result = 10 / x
        print(result)
    except ValueError:
        print("Input không hợp lệ")
    except ZeroDivisionError:
        print("Không thể chia cho 0")
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        print("Luôn được thực thi")

