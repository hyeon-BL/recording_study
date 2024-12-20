import 'package:flutter/material.dart';
import 'package:flutter_application_3/model_model/webtoon.dart';
import 'package:flutter_application_3/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key});

  final Future<List<WebtoonModel>> webtoons = ApiService.getTodayWebtoons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          elevation: 1,
          shadowColor: Colors.grey[100],
          backgroundColor: Colors.white,
          foregroundColor: Colors.green,
          title: const Center(
            child: Text(
              '오늘의 웹툰',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.w600),
            ),
          ),
        ),
        body: FutureBuilder(
            // 기다림 상태를 보여주는 위젯
            future: webtoons,
            builder: (context, snapshot) {
              // snapshot: future의 결과를 가지고 있음
              if (snapshot.hasData) {
                return Column(
                  children: [
                    SizedBox(height: 50),
                    Expanded(child: makeList(snapshot)),
                  ],
                );
              }
              return const Center(
                child: CircularProgressIndicator(),
              );
            }));
  }

  ListView makeList(AsyncSnapshot<List<WebtoonModel>> snapshot) {
    return ListView.separated(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
        // ListView: 스크롤 가능한 리스트(builder: 동적인 리스트 생성)
        itemBuilder: (context, index) {
          print(index);
          var webtoon = snapshot.data![index];
          return Column(
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
                  webtoon.thumb,
                  headers: const {
                    "User-Agent":
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                  },
                ),
              ),
              SizedBox(height: 10),
              Text(
                webtoon.title,
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.w600),
              ),
            ],
          );
        },
        separatorBuilder: (context, index) => SizedBox(width: 40),
        // separatorBuilder: 리스트의 각 요소 사이에 구분선을 추가
        scrollDirection: Axis.horizontal,
        itemCount: snapshot.data!.length);
  }
}
