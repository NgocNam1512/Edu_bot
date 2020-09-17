## intent:greet
- hey
- hello
- hi
- xin chào
- chào
- chào cháu
- chào cậu
- alo
- có ai ở đây không?

## intent:bot_challenge
- bạn có thể làm gì
- show chức năng
- chức năng
- mày có thể làm gì
- tôi muốn hỏi vài thứ
- tôi hỏi này

## intent:thanks
- cảm ơn cháu
- cảm ơn nha
- thankyou
- thank
- thanks

## intent:goodbye
- tạm biệt
- Bye
- tạm biệt nhé
- chào tạm biệt
- bai bai

## intent:ask_fee_tutor
- tiền [học phí](fee_tutor) là bao nhiêu
- Hết bao nhiêu [học phí](fee_tutor)
- Kì này tiền [học phí](fee_tutor) của con tôi là bao nhiêu
- Giá [học phí](fee_tutor)

## intent:ask_menu
- Trưa [nay]{"entity": "time", "value": "hôm nay"}
 con tôi [ăn gì](menu)
- [Bữa trưa](menu) có những gì
- con tôi [ăn gì](menu) [hôm nay](time)
- [thực đơn](menu) [hôm nay](time) có gì
- [ăn uống](menu) ra sao
- [ăn trưa](menu)
- thực đơn [hôm qua](time) gồm những món gì?
- [Hôm qua]{"entity": "time", "value": "hôm qua"} các cháu ăn gì ở trường?
- thực đơn ngày [20/7](time)
- Món [ăn trưa](menu) nay?
- Trưa [nay]{"entity": "time", "value": "hôm nay"} con tôi [ăn gì](menu)
- [Hôm nay]{"entity": "time", "value": "hôm nay"} có những [món gì](menu)
- [Thực đơn](menu) [hôm nay](time)
- [Hôm nay]{"entity": "time", "value": "hôm nay"} có [món gì](menu)
- [Ăn gì](menu) trưa [nay]{"entity": "time", "value": "hôm nay"}
- [Nay]{"entity": "time", "value": "hôm nay"} con tôi [ăn gì](menu)
- [Hôm nay]{"entity": "time", "value": "hôm nay"} các cháu [ăn gì](menu)?
- [Hôm qua]{"entity": "time", "value": "hôm nay"} con tôi [ăn gì](menu)?
- Ngày [mai]{"entity": "time", "value": "ngày mai"} [thực đơn](menu) ra sao

## intent:tuyen_sinh_doi_tuong
- Đối tượng [tuyển sinh](tuyen_sinh) của trường?
- Trưởng [tuyển](tuyen_sinh) những đối tượng nào?
- Học sinh ở Cầu Giấy có được học không?
- Gia đình tôi có sổ hộ khẩu ở Nam Từ Liêm thì có [nhập học](tuyen_sinh) cho con được không?
- Trường [tuyển](tuyen_sinh) học sinh có hộ khẩu ở đâu?
- Trường [tuyển](tuyen_sinh) học sinh ở đâu?
- Trường tuyển đối tượng học sinh nào

## intent:tuyen_sinh_thoi_gian_cach_thuc
- [Thời gian](duration) [tuyển sinh](students_number) là khi nào?
- [thời gian](duration) [tuyển sinh](students_number)
- Đăng kí [tuyển sinh](students_number) vào lúc nào?
- Bao giờ thì hết [hạn](duration) [tuyển sinh](students_number)?
- [Thời hạn](duration) [tuyển sinh](students_number)?

## intent:tuyen_sinh_so_luong
- Trường [tuyển](tuyen_sinh) [bao nhiêu học sinh](students_number) ?
- trường tuyển bao nhiêu học sinh năm nay
- năm nay trường tuyển bao nhiêu học sinh
- Số lượng [tuyển sinh](tuyen_sinh)
- Trường [tuyển sinh](tuyen_sinh) [bao nhiêu bạn](students_number)
- Năm nay trường [tuyển sinh](tuyen_sinh) nhiều không
- [Tuyển sinh](tuyen_sinh) [mấy bạn](students_number)?
- Năm nay trường [tuyển sinh](tuyen_sinh) [bao nhiêu lớp](classes_number)?
- Năm nay trường [tuyển sinh](tuyen_sinh) [bao nhiêu lớp](classes_number) nhỉ?
- Trường [tuyển sinh](tuyen_sinh) [bao nhiêu lớp](classes_number)
- [Số lớp](classes_number) [tuyển sinh](tuyen_sinh)
- [Tuyển sinh](tuyen_sinh) [bao nhiêu lớp](classes_number)?
- số lớp [tuyển sinh](tuyen_sinh)
- trường tuyển bao nhiêu học sinh

## intent:tuyen_sinh_ho_so
- [Hồ sơ](ho_so) [tuyển sinh](tuyen_sinh)
- [Hồ sơ](ho_so) [tuyển sinh](tuyen_sinh) bao gồm những gì?
- Cần chuẩn bị [hồ sơ](ho_so) gồm những gì
- [Hồ sơ](ho_so) [tuyến sinh](tuyen_sinh) cần gì?
- Chuẩn bị [hồ sơ](ho_so) ra sao
- Quy định về [hồ sơ](ho_so) của học sinh

## intent:ask_about_child
- [hôm nay](time) cháu có [ngoan](attitude) không?
- Cháu [hôm nay](time) có [nghịch](attitude) không?
- Cháu có [ngủ trưa](attitude) không?
- Cháu có [quấy khóc](attitude) không?
- [hôm nay](time) cháu ăn được mấy bát?
- Cháu [hôm nay](time) [ngoan](attitude) không?
- Cháu [hôm nay](time) trên lớp thế nào?
- [hôm nay](time) trên lớp tình hình cháu thế nào?
- Nay cháu có [ngủ trưa](attitude) không?
- [Hôm nay]{"entity": "time", "value": "hôm nay"} cháu có [quấy](attitude) không?
- Bé ở lớp thế nào?
- [Hôm qua]{"entity": "time", "value": "hôm qua"} cháu ở lớp học có [ngoan](attitude) không?
- hôm nay con tôi thế nào?
- Hôm nay con tôi thế nào?
- nhận xét của giáo viên
- Nhận xét của giáo viên về con tôi
- xem nhận xét giáo viên
- [hôm nay](time) cháu có [tập trung](attitude) học bài không

## intent:ask_score
- [hôm nay](time) con tôi có [điểm](score) gì không?
- [Điểm](score) [hôm nay](time) 
- [Điểm](score) [miệng](daily_score) môn [Tiếng anh]{"entity": "subject", "value": "Anh Văn"}
- [Điểm](score) ngày [hôm nay](time)
- [Điểm](score) hàng ngày môn [Anh Văn](subject)
- [Điểm](score) kiểm tra [giữa kỳ](mid_score)
- [Điểm](score) kiểm tra [giữa kì](mid_score) của con tôi là bao nhiêu?
- [Điểm](score) kiểm tra [giữa kỳ](mid_score) của con tôi
- [Điểm](score) [giữa kì](mid_score)
- [Điểm](score) kiểm tra [cuối kỳ](end_score)
- [Điểm](score) kiểm tra [cuối kỳ](end_score) của con tôi là bao nhiêu?
- [Điểm](score) kiểm tra [cuối kì](end_score) của con tôi
- [Điểm](score) [cuối kỳ](end_score) môn [Toán](subject) là bao nhiêu
- [Điểm](score) [cuối kì](end_score) môn [Tiếng Việt](subject) là bao nhiêu?
- [Điểm](score) [mỹ thuật]{"entity": "subject", "value": "Mĩ Thuật"}
- [Điểm](score) môn [anh]{"entity": "subject", "value": "Anh Văn"}
- [Điểm](score) [miệng](daily_score) ngày [18/9](time)

## intent:ask_timetable
- [Thời khóa biểu](timetable)
- [Thời khóa biểu](timetable) [ngày mai](time)
- [Thời khóa biểu](timetable) mai thế nào
- [Mai]{"entity": "time", "value": "ngày mai"} con tôi học những gì
- [ngày mai](time) con tôi học môn gì
- [hôm qua](time) lớp con tôi có những môn gì
- [Thời khóa biểu](timetable) [ngày mai](time) có những môn gì
- [thời khóa biểu](timetable) ngày [18/9](time)
- ngày [20/9](time) con tôi học những môn gì?
- [thời khóa biểu](timetable) ngày [hôm qua](time)

## intent:give_phone_number
- [12345678](phone_number)
- số điện thoại là [0352229999](phone_number)

## regex:phone_number
- 0[0-9]{9}

## lookup:time
data/time.txt

## lookup:subject
data/subjects.txt