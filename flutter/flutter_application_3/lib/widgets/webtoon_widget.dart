import 'package:flutter/material.dart';
import 'package:flutter_application_3/screens/detail_screen.dart';

class Webtoon extends StatelessWidget {
  final String title, thumb, id;

  const Webtoon(
      {super.key, required this.title, required this.thumb, required this.id});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      // 사용자의 터치 동작을 감지하는 위젯
      onTap: () {
        Navigator.push(
          // 화면 이동(사실은 widget을 stack에 쌓는 것)
          context,
          MaterialPageRoute(
            // builder를 통해 새로운 화면을 생성
            builder: (context) =>
                DetailScreen(title: title, thumb: thumb, id: id),
            // fullscreenDialog: true, // 전체 화면 다이얼로그로 설정
          ),
        );
      },
      child: Column(
        children: [
          Container(
            width: 250,
            clipBehavior: Clip.hardEdge, // 부모 위젯의 경계를 벗어나지 않도록 설정
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(15),
              boxShadow: [
                BoxShadow(
                  color: Color.fromRGBO(10, 10, 10, 0.5),
                  spreadRadius: 1,
                  blurRadius: 7,
                  offset: const Offset(0, 3),
                ),
              ],
            ),
            child: Image.network(
              thumb,
              headers: const {
                "User-Agent":
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
              },
            ),
          ),
          SizedBox(height: 10),
          Text(
            title,
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.w600),
          ),
        ],
      ),
    );
  }
}
