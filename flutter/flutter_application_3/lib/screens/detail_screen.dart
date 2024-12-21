import 'package:flutter/material.dart';
import 'package:flutter_application_3/models/webtoon.dart';
import 'package:flutter_application_3/services/api_service.dart';

class DetailScreen extends StatefulWidget {
  // widget.ㅁ으로 미리 정의된 변수에 접근 가능
  final String title, thumb, id;

  const DetailScreen(
      {super.key, required this.title, required this.thumb, required this.id});

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

class _DetailScreenState extends State<DetailScreen> {
  late Future<WebtoonDetailModel> webtoonDetail;
  late Future<List<WebtoonEpisodeModel>> webtoonEpisodes;
  // late -> constructor에서 초기화 불가능한 변수를 나중에 초기화

  @override
  void initState() {
    super.initState();
    webtoonDetail = ApiService.getWebtoonDetail(widget.id);
    webtoonEpisodes = ApiService.getWebtoonEpisodes(widget.id);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 1,
        shadowColor: Colors.grey[100],
        backgroundColor: Colors.white,
        foregroundColor: Colors.green,
        title: Text(
          widget.title,
          style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w600),
        ),
      ),
      body: Column(
        children: [
          SizedBox(height: 50),
          Center(
            child: Hero(
              // 화면 이동 시 애니메이션 효과를 주기 위해 사용
              tag: widget.id,
              child: Container(
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
                  widget.thumb,
                  headers: const {
                    "User-Agent":
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                  },
                ),
              ),
            ),
          ),
        ],
      ),
    ); // 새로운 화면을 생성(scaffold: 기본 앱 디자인 구조)
  }
}
