"""
Script tao du lieu mau cho DUE Book
Chay: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from books.models import Subject, Book
from users.models import UserProfile
from ratings.models import Rating
import random


class Command(BaseCommand):
    help = 'Tao du lieu mau cho ung dung DUE Book'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10, help='So luong nguoi dung mau')
        parser.add_argument('--books', type=int, default=30, help='So luong sach mau')
        parser.add_argument('--ratings', type=int, default=20, help='So luong danh gia mau')

    def handle(self, *args, **options):
        num_users = options['users']
        num_books = options['books']
        num_ratings = options['ratings']

        self.stdout.write('[*] Bat dau tao du lieu mau...\n')

        # Xoa du lieu cu
        self.stdout.write('[*] Xoa du lieu cu...')
        Rating.objects.all().delete()
        Book.objects.all().delete()
        Subject.objects.all().delete()
        self.stdout.write(' Done!\n')

        # Tao Subjects (Mon hoc)
        subjects_data = [
            {'name': 'Kinh te vi mo', 'code': 'KT101', 'description': 'Nguyen ly kinh te vi mo'},

            {'name': 'Thong ke kinh te', 'code': 'KT201', 'description': 'Phan tich thong ke trong kinh te'},
            {'name': 'Ke toan tai chinh', 'code': 'KT301', 'description': 'Nguyen ly ke toan'},
            {'name': 'Quan tri kinh doanh', 'code': 'QTKD101', 'description': 'Co so quan tri kinh doanh'},
            {'name': 'Marketing can ban', 'code': 'MKT101', 'description': 'Nguyen ly marketing'},
            {'name': 'Tai chinh tien te', 'code': 'TC101', 'description': 'He thong tai chinh tien te'},
            {'name': 'Luat kinh te', 'code': 'LAW101', 'description': 'Phap luat trong kinh doanh'},
            {'name': 'Toan cao cap', 'code': 'MATH101', 'description': 'Toan hoc dai hoc'},
            {'name': 'Tieng Anh thuong mai', 'code': 'ENG201', 'description': 'Tieng Anh chuyen nganh'},
            {'name': 'Kinh te luong', 'code': 'KT401', 'description': 'Mo hinh kinh te luong'},
            {'name': 'Quan tri nhan luc', 'code': 'HRM101', 'description': 'Quan ly nguon nhan luc'},
            {'name': 'Chien luoc kinh doanh', 'code': 'STR301', 'description': 'Lap chien luoc doanh nghiep'},
            {'name': 'Thuong mai dien tu', 'code': 'ECOM201', 'description': 'Kinh doanh truc tuyen'},
            {'name': 'Phan tich du lieu', 'code': 'DA101', 'description': 'Phan tich du lieu kinh te'},
        ]

        subjects = []
        for subject_data in subjects_data:
            subject = Subject.objects.create(**subject_data)
            subjects.append(subject)
            self.stdout.write(f'  [+] Tao mon hoc: {subject.name}')

        self.stdout.write(f'\n[+] Da tao {len(subjects)} mon hoc\n')

        # Tao Users
        users_data = [
            {
                'username': 'nguyenvan_a',
                'email': 'nguyenvana@due.edu.vn',
                'first_name': 'Nguyen Van',
                'last_name': 'An',
                'student_id': '2021001',
                'phone': '0901234567',
                'bio': 'Sinh vien nam 3, chuyen nganh Kinh te',
            },
            {
                'username': 'tranthi_b',
                'email': 'tranthib@due.edu.vn',
                'first_name': 'Tran Thi',
                'last_name': 'Binh',
                'student_id': '2021002',
                'phone': '0902345678',
                'bio': 'Sinh vien nam 3, chuyen nganh Marketing',
            },
            {
                'username': 'levan_c',
                'email': 'levanc@due.edu.vn',
                'first_name': 'Le Van',
                'last_name': 'Cuong',
                'student_id': '2021003',
                'phone': '0903456789',
                'bio': 'Sinh vien nam 4, chuyen nganh Tai chinh',
            },
            {
                'username': 'phamthi_d',
                'email': 'phamthid@due.edu.vn',
                'first_name': 'Pham Thi',
                'last_name': 'Dung',
                'student_id': '2021004',
                'phone': '0904567890',
                'bio': 'Sinh vien nam 2, chuyen nganh Ke toan',
            },
            {
                'username': 'hoangvan_e',
                'email': 'hoangvane@due.edu.vn',
                'first_name': 'Hoang Van',
                'last_name': 'Em',
                'student_id': '2021005',
                'phone': '0905678901',
                'bio': 'Sinh vien nam 3, chuyen nganh QTKD',
            },
        ]

        # Them them users ngau nhien
        first_names = ['Nguyen', 'Tran', 'Le', 'Pham', 'Hoang', 'Huynh', 'Phan', 'Vu', 'Vo', 'Dang']
        last_names = ['Van A', 'Thi B', 'Van C', 'Thi D', 'Van E', 'Thi F', 'Van G', 'Thi H', 'Van I', 'Thi K']

        for i in range(6, num_users + 1):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names) + str(i)
            users_data.append({
                'username': f'sinhvien_{i}',
                'email': f'sinhvien{i}@due.edu.vn',
                'first_name': first_name,
                'last_name': last_name,
                'student_id': f'2021{i:03d}',
                'phone': f'09{random.randint(10000000, 99999999)}',
                'bio': f'Sinh vien Dai hoc Kinh te',
            })

        users = []
        for user_data in users_data:
            try:
                user = User.objects.get(username=user_data['username'])
                created = False
            except User.DoesNotExist:
                user = User.objects.create(
                    username=user_data['username'],
                    email=user_data['email'],
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                )
                user.set_password('password123')
                user.save()
                created = True
            
            if created:
                profile = user.profile
                profile.student_id = user_data.get('student_id', '')
                profile.phone_number = user_data.get('phone', '')
                profile.bio = user_data.get('bio', '')
                profile.save()
                self.stdout.write(f'  [+] Tao user: {user.username}')
            users.append(user)

        self.stdout.write(f'\n[+] Da co {len(users)} nguoi dung\n')

        # Tao Books
        books_data = [
            {
                'title': 'Kinh te vi mo - Nguyen ly va ung dung',
                'author': 'N. Gregory Mankiw',
                'price': 80000,
                'original_price': 180000,
                'condition': 'good',
                'description': 'Sach con moi, khong ghi chu nhieu. Phien ban dich tieng Viet.',
            },
            {
                'title': 'Kinh te vi mo - Phan tich',
                'author': 'Paul Krugman',
                'price': 75000,
                'original_price': 165000,
                'condition': 'like_new',
                'description': 'Sach moi mua nhung khong dung den. Full trang.',
            },
            {
                'title': 'Thong ke kinh te',
                'author': 'Nguyen Van Dao',
                'price': 50000,
                'original_price': 120000,
                'condition': 'fair',
                'description': 'Sach co gach chan mot so phan, van doc tot.',
            },
            {
                'title': 'Nguyen ly Marketing',
                'author': 'Philip Kotler',
                'price': 90000,
                'original_price': 200000,
                'condition': 'new',
                'description': 'Sach moi 100%, chua qua su dung.',
            },
            {
                'title': 'Quan tri kinh doanh',
                'author': 'Peter Drucker',
                'price': 65000,
                'original_price': 150000,
                'condition': 'good',
                'description': 'Sach dung cho mon QTKD can ban.',
            },
            {
                'title': 'Ke toan tai chinh',
                'author': 'Nguyen Thi Lan',
                'price': 55000,
                'original_price': 130000,
                'condition': 'good',
                'description': 'Full bai tap va loi giai.',
            },
            {
                'title': 'Tai chinh tien te',
                'author': 'Frederic Mishkin',
                'price': 85000,
                'original_price': 190000,
                'condition': 'like_new',
                'description': 'Sach ban dich, con rat moi.',
            },
            {
                'title': 'Luat kinh te',
                'author': 'Pham Van Tuan',
                'price': 45000,
                'original_price': 100000,
                'condition': 'fair',
                'description': 'Sach cu nhung van con day du trang.',
            },
            {
                'title': 'Toan cao cap C1',
                'author': 'Nguyen Thua Hop',
                'price': 40000,
                'original_price': 95000,
                'condition': 'poor',
                'description': 'Sach cu, co ghi chu nhieu.',
            },
            {
                'title': 'Tieng Anh thuong mai',
                'author': 'Market Leader',
                'price': 70000,
                'original_price': 160000,
                'condition': 'good',
                'description': 'Kem CD audio.',
            },
        ]

        book_adjectives = ['Giao trinh', 'Bai tap', 'Huong dan', 'Tom tat', 'De cuong']
        conditions = ['new', 'like_new', 'good', 'fair', 'poor']

        books_created = 0
        for i, book_data in enumerate(books_data):
            seller = random.choice(users)
            subject = random.choice(subjects)
            book = Book.objects.create(
                title=book_data['title'],
                author=book_data.get('author', 'Tac gia'),
                subject=subject,
                price=book_data['price'],
                original_price=book_data.get('original_price'),
                condition=book_data.get('condition', 'good'),
                description=book_data.get('description', ''),
                seller=seller,
                status='available',
            )
            books_created += 1
            self.stdout.write(f'  [+] Tao sach: {book.title}')

        # Tao them sach ngau nhien
        for i in range(len(books_data) + 1, num_books + 1):
            subject = random.choice(subjects)
            adj = random.choice(book_adjectives)
            title = f'{adj} {subject.name} - T{random.randint(1, 999)}'
            condition = random.choice(conditions)
            price = random.randint(30000, 150000)
            original_price = int(price * random.uniform(1.5, 2.5))

            book = Book.objects.create(
                title=title,
                author=f'Tac gia {i}',
                subject=subject,
                price=price,
                original_price=original_price,
                condition=condition,
                description=f'Sach dung cho mon {subject.name}. Tinh trang {condition}.',
                seller=random.choice(users),
                status='available',
            )
            books_created += 1
            self.stdout.write(f'  [+] Tao sach: {book.title}')

        books = Book.objects.all()
        self.stdout.write(f'\n[+] Da tao {books_created} cuon sach\n')

        # Tao Ratings
        ratings_created = 0
        for i in range(num_ratings):
            seller = random.choice(users)
            reviewer = random.choice([u for u in users if u != seller])
            book = random.choice(books)
            rating_value = random.choices([3, 4, 5], weights=[1, 3, 6])[0]

            try:
                rating = Rating.objects.create(
                    seller=seller,
                    reviewer=reviewer,
                    book=book,
                    rating=rating_value,
                    comment=random.choice([
                        'Nguoi ban than thien, sach dung mo ta!',
                        'Giao dich nhanh gon, rat hai long.',
                        'Sach dep, gia hop ly.',
                        'Recommended! Se mua lai.',
                        'Tot, dung nhu mo ta.',
                        'Giao dich suon se.',
                    ])
                )
                ratings_created += 1
            except:
                pass

        self.stdout.write(f'\n[+] Da tao {ratings_created} danh gia\n')

        # Cap nhat reputation cho tat ca users
        for user in users:
            if hasattr(user, 'profile'):
                user.profile.update_reputation()

        self.stdout.write(self.style.SUCCESS('\n[OK] Hoan thanh tao du lieu mau!'))
        self.stdout.write('\n Thong ke:')
        self.stdout.write(f'   - Mon hoc: {Subject.objects.count()}')
        self.stdout.write(f'   - Nguoi dung: {User.objects.count()}')
        self.stdout.write(f'   - Sach: {Book.objects.count()}')
        self.stdout.write(f'   - Danh gia: {Rating.objects.count()}')
        self.stdout.write('\n Thong tin dang nhap:')
        self.stdout.write('   - Username: admin / Password: (da tao truoc do)')
        self.stdout.write('   - Username: nguyenvan_a / Password: password123')
        self.stdout.write('   - Cac user khac co password: password123\n')