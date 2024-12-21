import 'package:flutter/material.dart';
import 'package:flutter_application_3/models/webtoon.dart';
import 'package:flutter_application_3/services/api_service.dart';
import 'package:flutter_application_3/widgets/episode_widget.dart';
import 'package:shared_preferences/shared_preferences.dart';

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
  late SharedPreferences prefs;
  bool isFavorite = false;
  // late -> constructor에서 초기화 불가능한 변수를 나중에 초기화
  // SharedPreferences -> 앱의 설정 정보를 저장하는 클래스

  Future<void> initPrefs() async {
    prefs = await SharedPreferences.getInstance();
    final favoriteWebtoons = prefs.getStringList('favoriteWebtoons');
    if (favoriteWebtoons != null) {
      if (favoriteWebtoons.contains(widget.id)) {
        setState(() {
          isFavorite = true;
        });
      }
    } else {
      // favoriteWebtoons가 null일 경우 빈 리스트로 초기화
      await prefs.setStringList('favoriteWebtoons', []);
    }
  }

  onHeartTap() async {
    final favoriteWebtoons = prefs.getStringList('favoriteWebtoons');
    if (favoriteWebtoons != null) {
      if (isFavorite) {
        favoriteWebtoons.remove(widget.id); // 즐겨찾기에서 제거
      } else {
        favoriteWebtoons.add(widget.id); // 즐겨찾기에 추가
      }
    }
    await prefs.setStringList('favoriteWebtoons', favoriteWebtoons ?? []);
    setState(() {
      isFavorite = !isFavorite;
    });
  }

  @override
  void initState() {
    super.initState();
    webtoonDetail = ApiService.getWebtoonDetail(widget.id);
    webtoonEpisodes = ApiService.getWebtoonEpisodes(widget.id);
    initPrefs();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        actions: [
          IconButton(
            onPressed: onHeartTap,
            icon: Icon(isFavorite ? Icons.favorite : Icons.favorite_border),
          )
        ],
        elevation: 1,
        shadowColor: Colors.grey[100],
        backgroundColor: Colors.white,
        foregroundColor: Colors.green,
        title: Text(
          widget.title,
          style: const TextStyle(fontSize: 24, fontWeight: FontWeight.w600),
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 35, vertical: 50),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Hero(
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
                ],
              ),
              SizedBox(
                height: 25,
              ),
              FutureBuilder(
                future: webtoonDetail,
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    return Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(snapshot.data!.about,
                            style: const TextStyle(fontSize: 14)),
                        const SizedBox(height: 15),
                        Text(
                            '장르: ${snapshot.data!.genre} / 연령: ${snapshot.data!.age}',
                            style: const TextStyle(fontSize: 14)),
                      ],
                    );
                  }
                  return Text('Loading...');
                },
              ),
              SizedBox(height: 25),
              FutureBuilder(
                future: webtoonEpisodes,
                builder: (context, snapshot) {
                  if (snapshot.hasData) {
                    return Column(children: [
                      for (var episode in snapshot.data!)
                        Episode(
                          episode: episode,
                          webtoonId: widget.id,
                        ),
                    ]);
                  }
                  return Container();
                },
              ),
            ],
          ),
        ),
      ),
    ); // 새로운 화면을 생성(scaffold: 기본 앱 디자인 구조)
  }
}
