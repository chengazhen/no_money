# Công Cụ Tự Động Hóa Cursor Pro

## Lời Nhắc
Gần đây có người mang phần mềm này bán trên các trang thương mại, việc này nên hạn chế. Không phải cái gì cũng cần kiếm tiền.

## Tuyên Bố Giấy Phép
Dự án này sử dụng giấy phép [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).  
Điều đó có nghĩa là bạn có thể:  
- **Chia sẻ** — Sao chép và phân phối tác phẩm này trên mọi phương tiện hoặc định dạng.  
Nhưng phải tuân thủ các điều kiện sau:
- **Phi thương mại** — Không được sử dụng tác phẩm này cho mục đích thương mại.

## Hướng Dẫn Video
[Xem video hướng dẫn](https://www.bilibili.com/video/BV1QTckewELS/)

## Giới Thiệu Tính Năng
Tự động đăng ký tài khoản, tự động làm mới token, giải phóng đôi tay.

## Địa Chỉ Tải Về
[https://github.com/chengazhen/cursor-auto-free/releases](https://github.com/chengazhen/cursor-auto-free/releases)

## Lưu Ý Quan Trọng
1. **Hãy đảm bảo bạn đã cài đặt trình duyệt Chrome. Nếu chưa, [tải về tại đây](https://www.google.com/intl/en_pk/chrome/).**  
2. **Bạn cần đăng nhập vào tài khoản, dù tài khoản có hiệu lực hay không, đăng nhập là bắt buộc.**  
3. **Cần có kết nối mạng ổn định, ưu tiên sử dụng máy chủ nước ngoài. Không bật proxy toàn cầu.**

## Hướng Dẫn Cấu Hình
- Cần sử dụng email theo tên miền Cloudflare. Hãy tìm hiểu cách sử dụng.  
- **(Rất quan trọng)** Cần sử dụng email tạm thời từ temp-mail.plus. Hãy tìm hiểu cách sử dụng.  
- Chuyển tiếp email từ tên miền Cloudflare sang temp-mail.plus.  
- Tải tệp `.env.example` về thư mục gốc của chương trình và đổi tên thành `.env`.

### Cấu hình tệp `.env`:
```bash
DOMAIN='xxxxx.me'    # Tên miền email của bạn (tự tìm hiểu cách sử dụng Cloudflare email)
TEMP_MAIL='xxxxxx'   # Tiền tố email tạm thời (không cần hậu tố)
```
Ví dụ:
```bash
DOMAIN='wozhangsan.me'
TEMP_MAIL='ccxxxxcxx'
```
Chương trình sẽ tự tạo ngẫu nhiên email với đuôi `@wozhangsan.me`.

## Cách Chạy Chương Trình

### Phiên Bản Mac
1. Mở Terminal và truy cập thư mục chứa ứng dụng.  
2. Cấp quyền thực thi tệp:  
```bash
chmod +x ./CursorPro
```  
3. Chạy chương trình:
   - Trong Terminal:  
```bash
./CursorPro
```  
   - Hoặc nhấp đôi vào tệp trong Finder.  

Nếu gặp lỗi, tham khảo [giải pháp](https://sysin.org/blog/macos-if-crashes-when-opening/).

### Phiên Bản Windows
Nhấp đúp chuột vào tệp `CursorPro.exe`.

## Xác Minh Hiệu Quả
Sau khi chạy script, khởi động lại trình chỉnh sửa. Nếu tài khoản hiển thị giống như trong log, chương trình đã hoạt động thành công.

## Lưu Ý Khi Sử Dụng
1. Yêu cầu môi trường:
   - Kết nối mạng ổn định.
   - Quyền hệ thống đủ cao.

2. Trong quá trình sử dụng:
   - Chờ chương trình tự hoàn tất.
   - Đợi thông báo "hoàn thành" trước khi đóng chương trình.

## Giải Quyết Vấn Đề Thường Gặp
1. Chương trình bị treo:
   - Kiểm tra kết nối mạng.
   - Khởi động lại chương trình.

## Tuyên Bố Miễn Trừ
Công cụ này chỉ dành cho mục đích học tập và nghiên cứu. Người dùng tự chịu trách nhiệm về mọi hậu quả. Nghiêm cấm sử dụng cho mục đích thương mại. Vi phạm giấy phép sẽ chịu trách nhiệm pháp lý.

## Nhật Ký Cập Nhật
- **2025-01-09**: Thêm log, chức năng tự xây dựng.  
- **2025-01-10**: Chuyển sang email tên miền Cloudflare. 
- **2025-01-11**: Thêm chức năng tự động xây dựng, thêm chức năng tự động xây dựng, thêm chức năng tự động xây dựng.

Một phần mã nguồn đến từ [gpt-cursor-auto](https://github.com/hmhm2022/gpt-cursor-auto).
